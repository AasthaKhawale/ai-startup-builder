from utils.financial_engine import calculate_projection

def run_finance():
    projection = calculate_projection(
        initial_users=100,
        price=10,
        growth_rate=0.1
    )

    return {
        "12_month_revenue_projection": projection
    }