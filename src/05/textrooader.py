from langchain_community.document_loaders import TextLoader

loader = TextLoader(
    file_path="D:/프로젝트/Langgraph_Modular_RAG/data/notice.txt",
    encoding="utf-8"
)

documents = loader.load()

print(f"문서길이: {len(documents)}")
print(f"문서내용: {documents[0].page_content}")
print(f"메타데이터: {documents[0].metadata}")