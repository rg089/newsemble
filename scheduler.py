"""
Authors: Rishabh Gupta (rg089), Vishal Singhania (vishalvvs)
"""

from scraper import Data
from db import connect

data = Data.collect(source="all")
coll = connect()
coll.remove()   # Removes all the documents in the database 
coll.insert_many(data)    # Inserts the new ones
