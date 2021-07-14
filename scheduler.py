"""
Authors: Rishabh Gupta (rg089), Vishal Singhania (vishalvvs)
"""

from scraper import Data
from db import connect

data = Data.collect(source="all")
recent,dataset = connect()
recent.remove()
recent.insert_many(data)
for i in data:
    try:
        dataset.insert_one(i)
    except:
        continue
# dataset.insert_many(data)
