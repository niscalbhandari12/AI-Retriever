import bs4
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import RetrievalQA
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline,AutoModelForSeq2SeqLM
from Retriever import CustomRetriever


model_id = 'google/flan-t5-small'
#model_id = 'facebook/blenderbot-1B-distill'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Context: {context}
Question: {question}
Only return the helpful answer below and nothing else.
Helpful answer:
"""

secondtemplate= """Question: {question}
Answer: Let's think step by step.
"""
prompt1 = PromptTemplate(template=secondtemplate, input_variables=["question"])
#llm = Ollama(model="llama2")

pipe = pipeline(
    'text2text-generation',
    model = model, 
    tokenizer=tokenizer,
    max_length=1000
)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'})
db = FAISS.load_local("faiss", embeddings,allow_dangerous_deserialization=True)
retriever = db.as_retriever(search_kwargs={'k': 3})

local_llm = HuggingFacePipeline(pipeline=pipe)

# llm_chain = LLMChain(llm=local_llm,
#                         prompt=prompt1)

#print(llm_chain.run('who is nischal? '))




# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2",
#     model_kwargs={'device': 'cpu'})


prompt = PromptTemplate(
    template=template,
    input_variables=['context', 'question'])

customRetriever = CustomRetriever()
qa_llm = RetrievalQA.from_chain_type(llm=local_llm,
                                     chain_type='stuff',
                                     retriever=customRetriever,
                                     return_source_documents=True,
                                     chain_type_kwargs={'prompt': prompt})


# prompt = "Who has worked in ERP system? What is their favorite color?"
# output = qa_llm({'query': prompt})
# print(output["result"])

def get_prompt():
    print("Type 'exit' to quit")

    while True:
        prompt = input("Enter a prompt: ")

        if prompt.lower() == 'exit':
            print('Exiting...')
            break
        else:
            try:
                print(retriever.get_relevant_documents(prompt))
                output = qa_llm({'query': prompt})
                print(output["result"])
            except Exception as e:
                print(e)

get_prompt()