import pymongo as pm
from pymongo import MongoClient
from scraper import Data
# to establish the connection with the cluster
def con():
  client = MongoClient("mongodb+srv://Vishal:vvs123@newsemble.j40x6.mongodb.net/News?retryWrites=true&w=majority")

  #Db name and Collection Name
  db = client["News"]
  collection = db["scraper"]
  return collection



