from utils.web_search import search_web
from utils.vector_store import create_vector_store
from utils.json_parser import extract_json
from core.llm import get_llm

llm = get_llm()

def run_research(idea: str):
    print("Searching web...")
    search_results = search_web(idea + " market size growth trends")
    
    search_results = search_web(idea + " market size growth trends")

    if not search_results:
     print("Web search returned no results. Using fallback research.")
    search_results = [f"General market information about {idea}."]

    vector_store = create_vector_store(search_results)

    context = "\n".join(search_results)

    prompt = f"""
    Based on the following real market data:

    {context}

    Provide structured market research in JSON:

    {{
        "market_size": "",
        "growth_rate": "",
        "key_trends": []
    }}
    """

    response = llm.invoke(prompt)
    return extract_json(response), vector_store