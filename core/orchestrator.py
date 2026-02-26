from agents.research_agent import run_research
from agents.strategy_agent import run_strategy
from agents.finance_agent import run_finance
from agents.critic_agent import run_critic
from agents.debate_agents import (
    run_pro_agent,
    run_risk_agent,
    run_judge_agent
)
from utils.database import save_startup


class StartupOrchestrator:

    def run(self, idea: str):

        print("\n=== Running Research Agent ===")
        research, vector_store = run_research(idea)

        retry_count = 0
        max_retries = 1
        strategy = None
        critic = None

        # -------------------------
        # STRATEGY + CRITIC LOOP
        # -------------------------
        while retry_count <= max_retries:

            print("\n=== Running Strategy Agent ===")
            strategy = run_strategy(idea, vector_store)

            print("\n--- DEBUG: STRATEGY OUTPUT ---")
            print(strategy)
            print("Strategy Type:", type(strategy))

            print("\n=== Running Critic Agent ===")
            critic = run_critic(strategy)

            print("Raw Critic Output:", critic)

            if critic is None:
                print("Invalid JSON from Critic. Retrying...")
                retry_count += 1
                continue

            # Flexible score handling
            raw_score = critic.get("score") or critic.get("rating")

            try:
                score = float(raw_score)
            except (ValueError, TypeError):
                print("Invalid score format. Retrying...")
                retry_count += 1
                continue

            print(f"Parsed Critic Score: {score}")

            if score >= 7:
                print("Acceptable strategy quality reached.")
                break

            print(f"Strategy score low ({score}). Regenerating...")
            retry_count += 1

        # -------------------------
        # FINANCE
        # -------------------------
        print("\n=== Running Finance Agent ===")
        finance = run_finance()

        # -------------------------
        # DEBATE MODE
        # -------------------------
        print("\n=== Running Pro Agent ===")
        pro = run_pro_agent(strategy)

        print("\n=== Running Risk Agent ===")
        risk = run_risk_agent(strategy)

        print("\n=== Running Judge Agent ===")
        judge = run_judge_agent(pro, risk)

        # -------------------------
        # FINAL STRUCTURED RESULT
        # -------------------------
        final_result = {
            "idea": idea,
            "analysis": {
                "research": research,
                "strategy": strategy,
                "finance": finance,
                "critic": critic,
                "pro_analysis": pro,
                "risk_analysis": risk,
                "judge_decision": judge
            },
            "metadata": {
                "retries_used": retry_count,
                "status": "completed"
            }
        }

        # -------------------------
        # SAVE TO DATABASE
        # -------------------------
        save_startup(idea, final_result)

        print("\n=== Startup Analysis Completed & Saved ===")

        return final_result