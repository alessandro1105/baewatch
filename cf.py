from surprise import KNNWithZScore

# To use user-based cosine similarity
sim_options = {
    "name": "pearson",
    "user_based": True,  # Compute similarities between users
    "min_support": 10,
}
cf = KNNWithZScore(sim_options=sim_options)