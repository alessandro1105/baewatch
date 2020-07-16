from surprise import KNNWithZScore
from surprise.model_selection import GridSearchCV
from data import data

# Parameters to tune
sim_options = {
    "name": [
        "cosine",
        "pearson"
    ],
    "user_based": [True],  # We want to use an user base collaborative filter
    "min_support": [10, 100, 1000],
}

# Gridsearch to best tune the collaborative filtering
param_grid = {"sim_options": sim_options}
gs = GridSearchCV(KNNWithZScore, param_grid, measures=["rmse", "mae"], cv=3)

# Fit
gs.fit(data)

# Get the best
print(gs.best_score["rmse"])
print(gs.best_params["rmse"])