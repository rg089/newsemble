from scraper import Data
from db import con

data = Data.collect(source="all")
coll = con()
coll.remove()   # Removes all the documents in the database 
coll.insert_many(data)    # Inserts the new ones
