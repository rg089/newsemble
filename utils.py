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

def convert_to_datetime(articles):
    mapper = {"IT": "%B %d, %Y %H:%M", "TH": "%B %d, %Y %H:%M", "TOI": "%b %d, %Y, %H:%M",
              "NDTV": "%B %d, %Y %H:%M", "TIE": "%B %d, %Y %H:%M:%S"}
    for i, article in enumerate(articles):
        time_strformat = mapper[article["source"]]
        time = article["time"]
        time_conv = datetime.strptime(time, time_strformat)
        articles[i]["time"] = time_conv

    return articles


def read_data_db(source):
    coll, _ = connect()
    source = source.upper()
    if source == "ALL":
        return list(coll.find({},{"_id":0}))
    else:
        return list(coll.find({"source":source},{"_id":0}))
   

    


