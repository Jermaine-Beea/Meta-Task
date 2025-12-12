from individual_steps.step5 import query_rewriting_pack

def safe_rag_run(question, retries=3):
    """
    Run the RAG pipeline with basic retry logic.
    """
    for attempt in range(retries):
        try:
            resp = query_rewriting_pack.run(question)

            if resp is None or str(resp).strip() == "":
                raise ValueError("Empty LLM response.")

            return resp

        except Exception as e:
            print(f"⚠️ Error: {e}")
            print(f"🔁 Retrying ({attempt+1}/{retries})...")

    return "❌ Could not generate a valid answer after retries."

print("\nRAG Interactive Mode")
print("Ask any question about your PDF.")
print("Type 'end' to exit.\n")

# Interactive Q&A loop
while True:
    user_question = input("🟦 Enter your question: ").strip()

    if user_question.lower() == "end":
        print("\n👋 Session ended.")
        break

    print("\n🔍 Retrieving answer...\n")

    # Run the question through the RAG pipeline
    response = safe_rag_run(user_question)

    print("\n──────────────────────────────────────────────")
    print("❓ QUESTION:")
    print(user_question)
    print("\n🧠 ANSWER:")
    print(response)
    print("──────────────────────────────────────────────\n")
