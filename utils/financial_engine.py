def calculate_projection(initial_users, price, growth_rate):
    projection = []
    users = initial_users

    for month in range(12):
        revenue = users * price
        projection.append(round(revenue, 2))
        users = users * (1 + growth_rate)

    return projection