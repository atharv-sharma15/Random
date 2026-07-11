from build_knowledge_base import collection
from search import search_multi_vehicle
from video_lookup import load_all_vehicles
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

all_vehicles = load_all_vehicles()


def answer_question(collection, user_query):
    # Retrieve relevant chunks, balanced across vehicles if it's a comparison
    retrieved_chunks = search_multi_vehicle(collection, user_query, all_vehicles)

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
                "You are a friendly, confident Mahindra showroom salesperson talking to a customer "
                "face-to-face. Speak naturally and briefly, like a real conversation — 2-4 short "
                "sentences, no bullet points, no headers, no markdown formatting, no long lists. "
                "Use ONLY the specs and facts given in the provided context — never invent a spec "
                "that isn't there. You MAY reason, compare, and recommend (e.g., which vehicle suits "
                "city driving) based on the actual specs given, the way a real salesperson would in "
                "conversation, not like a spec sheet. If the context doesn't have enough information, "
                "say so briefly and naturally, and offer to check on it — don't just say you don't have it."
            ),
            "max_output_tokens": 300,
        },
    )

    return response.text