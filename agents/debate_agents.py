from core.llm import get_llm
from utils.json_parser import extract_json

llm = get_llm()

def run_pro_agent(strategy: dict):
    prompt = f"""
    Argue why this startup strategy will succeed:

    {strategy}

    Return JSON:
    {{
        "strengths": [],
        "opportunity_score": 0
    }}
    """
    return extract_json(llm.invoke(prompt))


def run_risk_agent(strategy: dict):
    prompt = f"""
    Argue why this startup strategy may fail:

    {strategy}

    Return JSON:
    {{
        "risks": [],
        "risk_score": 0
    }}
    """
    return extract_json(llm.invoke(prompt))


def run_judge_agent(pro: dict, risk: dict):
    prompt = f"""
    Based on:

    Strengths: {pro}
    Risks: {risk}

    Provide final evaluation.

    Return JSON:
    {{
        "final_score": 0,
        "confidence": 0,
        "verdict": ""
    }}
    """
    return extract_json(llm.invoke(prompt))