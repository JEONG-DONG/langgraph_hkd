from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(
    file_path="D:/프로젝트/Langgraph_Modular_RAG/data/notice.txt",
    encoding="utf-8"
)

documents = loader.load()

# 문서를 청크로 나누기
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30
)
chunks = text_splitter.split_documents(documents)

print(f"Chunk개수: {len(chunks)}")
print(f"첫번째: {chunks[0].page_content}")
print(f"두번째: {chunks[1].page_content}")