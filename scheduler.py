from scraper import Data
from db import con

data = Data.collect(source="all")
recent,dataset = con()
recent.remove()
recent.insert_many(data)
dataset.insert_many(data)
