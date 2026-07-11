from build_knowledge_base import collection
from search import search
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def answer_question(collection, user_query):
    # Retrieve top 3 relevant chunks
    retrieved_chunks = search(collection, user_query, n_results=3)

    # Combine them into context
    context = "\n\n".join(retrieved_chunks)

    # Generate answer
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=f"""
Context:
{context}
Question:
{user_query}
""",
        config={
            "system_instruction": (
                "Answer the user's question using ONLY the provided context. "
                "If the answer is not present in the context, reply: "
                "'I don't have that information.'"
            ),
            "max_output_tokens": 1024,
        },
    )

    return response.text