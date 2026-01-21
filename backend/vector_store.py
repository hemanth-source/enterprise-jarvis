from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from config import *

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index if not exists
if PINECONE_INDEX not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=PINECONE_INDEX,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region=PINECONE_ENV
        )
    )

index = pc.Index(PINECONE_INDEX)

model = SentenceTransformer(EMBEDDING_MODEL)

def embed_text(text):
    return model.encode(text).tolist()

def store_document(doc_id, text):
    embedding = embed_text(text)
    index.upsert([
        {
            "id": doc_id,
            "values": embedding,
            "metadata": {"text": text}
        }
    ])

def query_vector_db(query, top_k=3):
    embedding = embed_text(query)
    result = index.query(
        vector=embedding,
        top_k=top_k,
        include_metadata=True
    )
    return [match["metadata"]["text"] for match in result["matches"]]
