import ollama

def get_answer(question, chunks):
    context = ""
    for chunk in chunks:
        start = round(chunk["start"])
        end = round(chunk["end"])
        context += f"[{start}s to {end}s]: {chunk['text']}\n\n"

    prompt = f"""You are a helpful teaching assistant.

A student is asking a question based on an educational video.
Use only the context below to answer the question.
At the end of your answer mention the timestamp where this was discussed.

Context from video:
{context}

Student question: {question}

Answer:"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]