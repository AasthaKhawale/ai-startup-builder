import json
import re

def extract_json(text: str):
    if not text:
        return None

    # Remove markdown blocks
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    # Extract first JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        return None

    json_str = match.group()

    # Remove trailing commas (common LLM mistake)
    json_str = re.sub(r",\s*}", "}", json_str)
    json_str = re.sub(r",\s*]", "]", json_str)

    try:
        return json.loads(json_str)
    except Exception as e:
        print("JSON Parsing Error:", e)
        print("Raw LLM Output:", text)
        return None