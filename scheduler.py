"""
Authors: Rishabh Gupta (rg089), Vishal Singhania (vishalvvs)
"""

from scraper import Data
from db import connect

data = Data.collect(source="all")
recent,dataset = connect()
recent.remove()
recent.insert_many(data)
dataset.insert_many(data)
