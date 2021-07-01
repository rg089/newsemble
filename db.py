"""
Authors: Vishal Singhania (vishalvvs)
"""

from pymongo import MongoClient
import os

def connect():
  password = os.environ.get("password")
  client = MongoClient("mongodb+srv://Vishal:{password}@newsemble.j40x6.mongodb.net/News?retryWrites=true&w=majority")

  #Db name and Collection Name
  db = client["News"]
  collection = db["scraper"]
  return collection



