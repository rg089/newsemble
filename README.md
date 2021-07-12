# NEWSEMBLE
API for fetching data from news websites (Indian)

[Website](http://www.newsemble.ml/news/)

> Newsemble is a programmatic implementation of web scraping. This API has been built using Python, BeautifulSoup and MongoDB. 
  Newsemble retrieves the news articles from some Indian news websites namely Times of India, India Today, The Hindu, NDTV and The Indian Express. 
  Developers can make use of this API to fetch the news dataset with elements such as the headlines, content, source, link and time.  
  
  
<hr style="border:2px solid gray"> </hr>

## Table of contents
* [Technologies](#technologies)
* [File Structure and Description](#file-structure-and-description)
* [Getting started](#getting-started)


<hr style="border:2px solid gray"> </hr>
	
## Technologies
Project is created with:
* Python 3
* PyMongo

<hr style="border:2px solid gray"> </hr>

## File Structure and Description

* app.py - Flask code for the API
* scraper.py  - Collection of scrapers for the various news sites.
* db.py - Connecting and Using MongoDB
* utils.py - Utility Functions
* scheduler.py - Scheduler 
* Procfile - Pointer to the location (for cloud)
* requirements.txt - Python Requirments 


<hr style="border:2px solid gray"> </hr>

## Getting-started
This project can be accessed by using following setup

**Request format**
```
$ import requests
$ url = "http://www.newsemble.ml/news/"
$ requests.get(url).json()

```

**Response format**
```
{   ‘link’      :  $source_link$,
    ‘content’   :  $content_text$,    
    ‘source’    :  $news_source$,
    ‘title’     :  $headline$’, 
    ‘time       :  $date_time_of_article$  
 }
```
**Sample output**

![image](https://user-images.githubusercontent.com/52444089/125032819-1f5b3580-e0ac-11eb-9662-efa79dc0e099.png)

## Authors
1. Rishabh Gupta (rg089)
2. Vishal Singhania (vishalvvs)
3. Roshan Kumar (roshankumarg529)
