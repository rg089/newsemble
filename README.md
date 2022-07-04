<h1 align="center"> :newspaper: Newsemble :newspaper: </h1>

<p align="center">
  <br>
	<a href="http://www.newsemble.ml/news/"><img src="https://user-images.githubusercontent.com/66423362/125942926-17368ab4-7513-44b8-978f-1b013f7e08a3.png" alt="Logo"></a><br>
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
	
[![GitHub release](https://img.shields.io/github/release/rg089/newsemble.svg)](https://github.com/rg089/newsemble/releases/)
[![Visits Badge](https://badges.pufler.dev/visits/rg089/newsemble)](https://badges.pufler.dev)
![Stars Badge](https://img.shields.io/github/stars/rg089/newsemble.svg)
![Fork Badge](https://img.shields.io/github/forks/rg089/newsemble.svg)
[![Github all releases](https://img.shields.io/github/downloads/rg089/newsemble/total.svg)](https://github.com/rg089/newsemble/releases/)
![watchers Badge](https://img.shields.io/github/watchers/rg089/newsemble.svg)

</h1>



<h1 align="center"> :bookmark: About :bookmark: </h1><br>

<p align="center">
	<a href="https://medium.com/@rg089/newsemble-3311d2dc9817"><b>Blog Post</b></a>
</p>

> Newsemble is an API that provides easy access to the current news for programmatic analysis. It has been built using Python, BeautifulSoup and MongoDB.<br> 
  The data is scraped from [these news websites](#gear-currently-supported-sites) every hour, stored in a database on the cloud and whenever requested, the most recent articles are promptly served.<br>
  Developers can make use of this API to fetch current data with each article having the following fields: <br>***Headlines, Content, Source, Link and Time***.  

<hr style="border:2px solid gray"> </hr><br>

## :spiral_notepad: Table of contents
* [Technologies](#computer-technologies)
* [File Structure and Description](#open_file_folder-file-structure-and-description)
* [Pipeline](#hammer_and_wrench-pipeline)
* [Getting started](#rocket-getting-started)
* [Currently Supported Sites](#gear-currently-supported-sites)


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

## :hammer_and_wrench: Pipeline
![Newsemble pipeline](https://user-images.githubusercontent.com/52444089/125912546-d572c104-9c64-4237-a1f8-81228f8a0774.png)

## :rocket: Getting-started
This project can be accessed by using following setup

**Links**

<TABLE BORDER="3">
	<TH>Links </TH>
       <TH>Description</TH>
	
   <TR>
      <TD>http://www.newsemble.ml/news</TD>
      <TD>Link to fetch all the data from all sources</TD>
   </TR>
  <TR>
      <TD>http://www.newsemble.ml/news/toi</TD>
      <TD>Link to fetch data from Times of India </TD>
  </TR>
<TR>
      <TD>http://www.newsemble.ml/news/th</TD>
      <TD>Link to fetch data from The Hindu </TD>
  </TR>
 <TR>
      <TD>http://www.newsemble.ml/news/tie</TD>
      <TD>Link to fetch data from The Indian Express </TD>
  </TR>
 <TR>
      <TD>http://www.newsemble.ml/news/ndtv</TD>
      <TD>Link to fetch data from NDTV news </TD>
  </TR>
<TR>
      <TD>http://www.newsemble.ml/news/it</TD>
      <TD>Link to fetch data from India Today </TD>
  </TR>
  
</TABLE>


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
    ‘title’     :  $headline$, 
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
