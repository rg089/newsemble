"""
Authors: Vishal Singhania (vishalvvs)
"""

from pymongo import MongoClient
import os

def connect():
  pwd = os.environ.get("pwd")
  client = MongoClient(f"mongodb+srv://rishabh:{pwd}@news.aj9zk.mongodb.net/newsumm?retryWrites=true&w=majority")

  #Db name and Collection Name
  db = client["News"]
  recent = db["scraper"]
  dataset = db["dataset"]

  return recent,dataset



