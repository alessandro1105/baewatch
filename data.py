from surprise import Dataset

# Load ml-100k dataset
data = Dataset.load_builtin("ml-100k")
users_n = 943
items_n = 1682
min_rating = 1
max_rating = 5