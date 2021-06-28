import pickle
from scraper import Data

# dump to pickle for instant access.

data = Data.collect(source="all")
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# connect to database.