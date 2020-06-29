from surprise import KNNWithMeans

# To use user-based cosine similarity
sim_options = {
    "name": "cosine",
    "user_based": True,  # Compute  similarities between items
}
cf = KNNWithMeans(sim_options=sim_options)