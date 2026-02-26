from core.llm import get_llm
from utils.json_parser import extract_json

llm = get_llm()

def run_critic(strategy_output: dict):
   prompt = f"""
   You are a strict business evaluator.
   Evaluate the following startup strategy:
   {strategy_output}

   Return ONLY valid JSON in this exact format:

   {{
    "score": <number between 1 and 10>,
    "feedback": "<short explanation>"
   }}

   Do not add extra text.
   Do not change field names.
   """

   response = llm.invoke(prompt)
   return extract_json(response)