"""
Authors: Vishal Singhania (vishalvvs), Rishabh Gupta (rg089)
"""

from flask import Flask
from flask_restful import Api, Resource
from utils import read_data_db

app = Flask(__name__)
api = Api(app)

class News(Resource):
    def get(self, source="all"):
        source = source.lower()
        papers = ["tie","toi","ndtv","it","th", "all"]
        if source in papers:
            return read_data_db(source)
        s = """
		The source should be one of the following: TIE/tie: The Indian Express, TOI/toi: Times of India, 
		NDTV/ndtv, IT/it: India Today, TH/th: The Hindu, ALL/all: A collection of all the above
		"""
        return s, 404

api.add_resource(News, "/news", "/news/","/news/<string:source>")
if __name__ == '__main__':
    app.run(debug=True)
