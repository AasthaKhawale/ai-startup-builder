import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.orchestrator import StartupOrchestrator

if __name__ == "__main__":

    idea = input("Enter startup idea: ")

    orchestrator = StartupOrchestrator()

    result = orchestrator.run(idea)

    print("\n--- RESEARCH ---")
    print(result["research"])

    print("\n--- STRATEGY ---")
    print(result["strategy"])

    print("\n--- FINANCE ---")
    print(result["finance"])

    print("\n--- CRITIC ---")
    print(result["critic"])