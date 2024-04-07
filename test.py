from FreeschemaLoader import CustomDocumentLoader


loader = CustomDocumentLoader("./text1.txt")
for doc in loader.lazy_load():
    print()
    print(type(doc))
    print(doc)