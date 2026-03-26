from langchain_community.document_loaders import TextLoader

loader=TextLoader("data.txt")
loader1=TextLoader("data.pdf")

document=loader.load()
document1=loader1.load()


print(document[0].page_content)
print(document1[0].page_content)