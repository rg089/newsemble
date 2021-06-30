"""
Authors: Vishal Singhania (vishalvvs)
"""

from pymongo import MongoClient

def connect():
  client = MongoClient("mongodb+srv://Vishal:vvs123@newsemble.j40x6.mongodb.net/News?retryWrites=true&w=majority")

  #Db name and Collection Name
  db = client["News"]
  collection = db["scraper"]
  return collection



