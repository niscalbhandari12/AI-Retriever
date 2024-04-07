from langchain_core.retrievers import BaseRetriever
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from FreeschemaLoader import CustomDocumentLoader
from typing import List


class CustomRetriever(BaseRetriever):

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        loader = CustomDocumentLoader("./text1.txt")
        loader = loader.load()
        return loader
