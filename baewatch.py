def baewatch(predictions, min_rating, max_rating):
    # Define a dictionary of costs
    costs = generate_costs(predictions, min_rating, max_rating)

    # Now we simply sort based on the costs
    costs.sort(key=lambda x: x[1])

    # Get the results
    return costs[0]

def generate_costs(predictions, min_rating, max_rating):
    # Define a dictionary of costs
    costs = []

    # Calculate the cost for each movie
    for ratings in predictions:
        for (item, rating) in ratings:
            # Calculate the cost
            cost = (max_rating - rating)**2

            found = False
            for i in range(len(costs)):
                if item == costs[i][0]:
                    costs[i][1] += cost
                    found = True
                    break

            if not found:
                costs.append([item, cost])

    return costs