from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_store(docs):
    # Safety check
    if not docs or len(docs) == 0:
        return None

    return FAISS.from_texts(docs, embedding_model)

def retrieve_context(vector_store, query):
    if vector_store is None:
        return ""

    docs = vector_store.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])