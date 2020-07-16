from baewatch import baewatch

# Now let's select group of users randomly
group = list(range(4))

# Get the predictions
min_rating = 1
max_rating = 5

predictions = [
    [
        ['1', 4],
        ['2', 5],
        ['3', 2],
        ['4', 2],
        ['5', 1],
        ['6', 5],
        ['7', 4],
        ['8', 5],
        ['9', 5],
        ['10', 5],
        ['11', 5],
        ['12', 4]
    ],
    [
        ['1', 3],
        ['2', 1],
        ['3', 2],
        ['4', 2],
        ['5', 1],
        ['6', 5],
        ['7', 4],
        ['8', 5],
        ['9', 5],
        ['10', 5],
        ['11', 4],
        ['12', 4]
    ],
    [
        ['1', 5],
        ['2', 1],
        ['3', 2],
        ['4', 2],
        ['5', 1],
        ['6', 4],
        ['7', 4],
        ['8', 5],
        ['9', 5],
        ['10', 5],
        ['11', 4],
        ['12', 4]
    ],

    [
        ['1', 2],
        ['2', 5],
        ['3', 2],
        ['4', 1],
        ['5', 1],
        ['6', 1],
        ['7', 2],
        ['8', 1],
        ['9', 1],
        ['10', 2],
        ['11', 2],
        ['12', 5]
    ]
]

# Predict the rating with the baewatch algoritm
(item, cost) = baewatch(predictions, min_rating, max_rating)

# Finish
print('The selected item is: ', item, ', with a cost of: ', cost)
for i in range(len(predictions)):
    for rating in predictions[i]:
        if rating[0] == item:
            print('For user: ', group[i], ' the prediction was: ', rating[1])