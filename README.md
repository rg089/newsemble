<h1 align="center"> :newspaper: Newsemble :newspaper: </h1>
<p align="center">
  <br>
	<b><i>An <a href="http://www.newsemble.ml/news/">API</a> for fetching the current news.</b></i>
  <br><br>
</p>

<h1 align="center">
<a href="https://www.python.org"> <img alt = "python" src= "https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen"/> </a>&nbsp; 
<a href="https://palletsprojects.com/p/flask/"> <img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/> </a> &nbsp; 
<a href="https://www.mongodb.com/"> <img alt="MongoDB" src ="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"/>&nbsp; </a>
<a href="https://www.heroku.com/"> <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/> </a>
</h1>


<h1 align = "center">
	
<!--[![Visits Badge](https://badges.pufler.dev/visits/rg089/newsemble)](https://badges.pufler.dev)&nbsp;--> 
![watchers Badge](https://img.shields.io/github/watchers/roshankumarg529/Data.svg)&nbsp;
![Stars Badge](https://img.shields.io/github/stars/rg089/newsemble.svg)&nbsp;
![Fork Badge](https://img.shields.io/github/forks/rg089/newsemble.svg)
	
</h1>



<h1 align="center"> :bookmark: About :bookmark: </h1><br>

> Newsemble is an API that provides easy access to the current news for programmatic analysis. It has been built using Python, BeautifulSoup and MongoDB.<br> 
  The data is scraped from [these news websites](#currently-supported-sites) every hour, stored in a database on the cloud and whenever requested, the most recent articles are promptly served.<br>
  Developers can make use of this API to fetch current data with each article having the following fields: <br>***Headlines, Content, Source, Link and Time***.  

<hr style="border:2px solid gray"> </hr><br>

## :spiral_notepad: Table of contents
* [Technologies](#technologies)
* [File Structure and Description](#file-structure-and-description)
* [Getting started](#getting-started)
* [Currently Supported Sites](#currently-supported-sites)


## :computer: Technologies
Newsemble is created with:

* Python 3
* Flask
* PyMongo
* BeautifulSoup

## :open_file_folder: File Structure and Description

* *app.py* - Flask code for the API
* *scraper.py*  - Collection of scrapers for the various news sites.
* *db.py* - Connecting and Using MongoDB
* *utils.py* - Utility Functions
* *scheduler.py* - Scheduler 
* *Procfile* - For Deployment
* *requirements.txt* - Python Requirments 

## :rocket: Getting-started
This project can be accessed by using following setup

**Request format**
```
$ import requests
$ url = "http://www.newsemble.ml/news/"
$ requests.get(url).json()
```

**Response format**
```
{   
    ‘link’      :  $source_link$,
    ‘content’   :  $content_text$,    
    ‘source’    :  $news_source$,
    ‘title’     :  $headline$’, 
    ‘time       :  $date_time_of_article$  
 }
```
**Sample output**

![image](https://user-images.githubusercontent.com/52444089/125032819-1f5b3580-e0ac-11eb-9662-efa79dc0e099.png)

## :gear: Currently Supported Sites
* [Times of India](https://timesofindia.indiatimes.com/news)
* [India Today](https://www.indiatoday.in/)
* [The Hindu](https://www.thehindu.com/)
* [NDTV](https://www.ndtv.com/)
* [The Indian Express](https://indianexpress.com/)

<hr style="border:2px solid gray"> </hr><br>

<h1 align="center">:pray: Thanks!</h1>

<p align="center">
  <b>All contributions are welcome and appreciated. :+1: </b><br>
	<b><i>If you liked this project, or found it useful in any way, please drop a :star2:!</b></i><br><br>
</p>

<h1 align="center"> :writing_hand: Authors :writing_hand: </h1>

<p align="center">
	  :black_nib: <a href="https://github.com/rg089">Rishabh Gupta</a><br>
	  :black_nib: <a href="https://github.com/vishalvvs">Vishal Singhania</a><br>
	  :black_nib: <a href="https://github.com/roshankumarg529">Roshan Kumar</a><br>
</p>
