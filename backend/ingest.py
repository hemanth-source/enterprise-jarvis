from vector_store import store_document

with open("../data/knowledge.txt", "r") as f:
    text = f.read()

chunks = text.split("\n\n")

for i, chunk in enumerate(chunks):
    store_document(f"doc-{i}", chunk)

print("✅ Knowledge ingested successfully")
