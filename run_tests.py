"""
Day 9 test runner — asks 10 real questions across all 5 vehicles
and writes each Q&A pair to test_results.txt.

Run this from your project root, with (venv) active:
    python run_tests.py
"""

from datetime import datetime
from build_knowledge_base import collection
from ragchatbot import answer_question

# 2 questions per vehicle x 5 vehicles = 10 questions.
# Mix of "in the data" and "borderline/not in the data" questions —
# a good test set should probe BOTH cases, not just the easy ones.
test_questions = [
    # XUV700
    "What is the mileage of the XUV700?",
    "Does the XUV700 have ADAS features?",
    # Scorpio-N
    "What is the price range of the Scorpio-N?",
    "Is 4WD available on the Scorpio-N?",
    # Thar
    "What engines are available in the Thar?",
    "Is the Thar a 5-seater?",  # deliberately tricky — it's a 4-seater
    # Bolero
    "What is the seating capacity of the Bolero?",
    "Does the Bolero come with a sunroof?",  # not in the data - tests fallback
    # Bolero Neo
    "What is the engine power of the Bolero Neo?",
    "How is the Bolero Neo different from the Bolero?",
]

def run_tests():
    results = []
    print(f"Running {len(test_questions)} test questions...\n")

    for i, question in enumerate(test_questions, start=1):
        print(f"[{i}/{len(test_questions)}] {question}")
        try:
            answer = answer_question(collection, question)
        except Exception as e:
            answer = f"ERROR: {e}"
        results.append((question, answer))
        print(f"  -> {answer[:80]}{'...' if len(answer) > 80 else ''}\n")

    with open("test_results.txt", "w", encoding="utf-8") as f:
        f.write("RAG Chatbot Test Results\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 70 + "\n\n")
        for i, (q, a) in enumerate(results, start=1):
            f.write(f"Q{i}: {q}\n")
            f.write(f"A{i}: {a}\n")
            f.write("-" * 70 + "\n\n")

    print(f"Done. Results written to test_results.txt")


if __name__ == "__main__":
    run_tests()