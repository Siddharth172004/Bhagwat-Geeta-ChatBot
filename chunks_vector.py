import json
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.document import Document
from langchain_huggingface import HuggingFaceEmbeddings

docs = JSONLoader(
    file_path="C:/Users/Siddharth/OneDrive/Desktop/Llm Project/Data/geeta.json",
    jq_schema=".[]",
    text_content=False
)
data = docs.lazy_load()

all_chunks = []

for doc in data:
    content = doc.page_content
    if isinstance(content, str):
        content = json.loads(content)
        doc.page_content = content   

    combined = content.get("HinMeaning", "") + " || " + content.get("EngMeaning", "") + " || " + content.get("PurPort","")

    all_chunks.append({
        "text": combined,
        "metadata": content
    })

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = []
for chunk in all_chunks:
    doc_a = Document(
        page_content=chunk["text"],
        metadata={"original_text": chunk["metadata"]}
    )
    documents.append(doc_a)

db = FAISS.from_documents(documents, embeddings)
db.save_local(r"C:\Users\Siddharth\OneDrive\Desktop\Llm Project\Vector Data")
