from data import data, users_n, items_n, min_rating, max_rating
from cf import cf
from baewatch import baewatch

# # Get the trainset
trainset = data.build_full_trainset()

# # First we need to train the collaborative filtering algoritm
cf.fit(trainset)

# Now let's select group of users randomly
group = [str(99), str(456), str(96), str(1)]

# Prepare the items on which users did not give any ratings (movies not watched)
items = [str(x) for x in range(1, items_n)]

for rating in data.raw_ratings:
    if rating[0] in group and str(rating[1]) in items:
        items.remove(str(rating[1]))

# Predict ratings for users into the group
predictions = []
for user in group:
    ratings = []
    # Predict
    for item in items:
        prediction = cf.predict(user, item)
        ratings.append((item, prediction.est))
    # Save
    predictions.append(ratings)

# Predict the rating with the baewatch algoritm
(item, cost) = baewatch(predictions, min_rating, max_rating)

# Finish
print('The selected item is: ', item, ', with a cost of: ', cost)
for i in range(len(predictions)):
    for rating in predictions[i]:
        if rating[0] == item:
            print('For user: ', group[i], ' the prediction was: ', rating[1])
