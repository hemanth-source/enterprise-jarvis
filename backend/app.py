from fastapi import FastAPI
from vector_store import query_vector_db
from llm import generate_answer

app = FastAPI()

@app.post("/chat")
def chat(query: str):
    context = query_vector_db(query)
    context_text = "\n".join(context)

    prompt = f"""
    You are an enterprise AI assistant.
    Use the context below to answer.

    Context:
    {context_text}

    Question:
    {query}
    """

    answer = generate_answer(prompt)
    return {"answer": answer}
