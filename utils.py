"""
Authors: Rishabh Gupta (rg089), Vishal Singhania (vishalvvs)
"""


from scraper import Data
import os
import pickle
from db import connect

def filter_source(data, source):
    if source == "all":
        return data
    data = list(filter(lambda x: x["source"].lower()==source, data))
    return data

def read_data(source):
    source = source.lower()
    fname = "data.pkl"
    if os.path.exists(fname):
        with open(fname, "rb") as f:
            data = pickle.load(f)
        data = filter_source(data, source)
    else:
        if source == "all":
            source = "toi"  # Changing source to prevent heroku timeout
        data = Data.collect(source)
    return data

def read_data_db(source):
    coll, _ = connect()
    source = source.upper()
        return list(coll.find({},{"_id":0}))
    else:
        return list(coll.find({"source":source},{"_id":0}))

    


