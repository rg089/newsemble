"""
Authors: Vishal Singhania (vishalvvs)
"""
import pymongo as pm
from pymongo import MongoClient
from scraper import Data
# to establish the connection with the cluster
def con():
  """
    Returns the Collection Objects of the Database
  """

  client = MongoClient(f"mongodb+srv://Vishal:{pwd}@newsemble.j40x6.mongodb.net/News?retryWrites=true&w=majority")
  #Db name and Collection Name
  db = client["News"]
  recent = db["scraper"]
  dataset = db["dataset"]

  return recent,dataset



