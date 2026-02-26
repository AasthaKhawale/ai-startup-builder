from core.llm import get_llm

llm = get_llm()

def run_strategy(idea: str, vector_store):

    context = ""

    if vector_store is not None:
        try:
            docs = vector_store.similarity_search(idea, k=3)
            context = "\n".join([doc.page_content for doc in docs])
        except Exception as e:
            print("Vector retrieval error:", e)

    prompt = f"""
    You are a startup strategy expert.

    Startup idea: {idea}

    Market context:
    {context}

    Create a detailed business strategy.

    Structure it clearly with:
    - Target Customer
    - Value Proposition
    - Revenue Model
    """

    response = llm.invoke(prompt)

    print("\n===== RAW STRATEGY OUTPUT =====")
    print(response)
    print("================================\n")

    # TEMPORARY: return raw text (not JSON)
    return {
        "raw_strategy": response
    }