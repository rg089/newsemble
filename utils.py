from scraper import Data
import os
import pickle

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