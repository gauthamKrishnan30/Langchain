from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader=TextLoader("data.txt")

doucments=loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=0)
docs=text_splitter.split_documents(doucments)

print(docs[0].page_content)