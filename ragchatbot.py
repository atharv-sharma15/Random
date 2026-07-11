# from google import genai



# context = "XUV700 mileage is 18 kmpl (diesel manual). XUV700 price range is 13.99 to 24.94 Lakh."
# question = "What is the price range of thar"

# response = client.models.generate_content(
#     model="gemini-flash-latest",
#     contents=f"Context: {context}\n\nQuestion: {question}",
#     config={
#         "system_instruction": (
#             "Answer the user's question using ONLY the provided context. "
#             "If the answer isn't in the context, say you don't have that information."
#         ),
#         "max_output_tokens": 300,
#     },
# )

# print(response.text)
from build_knowledge_base import collection
from search import search
import os
from google import genai
from search import search  # Your Day 7 search function




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

