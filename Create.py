from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# define what documents to load
loader = DirectoryLoader("./", glob="*.txt", loader_cls=TextLoader)

# interpret information in the documents
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=100,
    chunk_overlap=50)
texts = splitter.split_documents(documents)

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2",
#     model_kwargs={'device': 'cpu'})

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'})

# create and save the local database
db = FAISS.from_documents(texts, embeddings)
db.save_local("faiss")