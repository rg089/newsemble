# NEWSEMBLE
API for fetching data from news websites (Indian)

[Website](http://www.newsemble.ml/news/)

⭐ If you find the project helpful star us on GitHub  — it motivates us a lot!

> Newsemble is a programmatic implementation for web scrapping, this API has been built using python programming with beautiful soup web scrapping library. 
  Newsemble retrieves the news articles from the News websites namely Times of India (TOI), India Today, The Hindu, NDTV news and The Indian Express. 
  Developers can make use of this API to fetch the news dataset with the elements such as Headlines, Content, Source, link and time of release.  
  
  
  
<hr style="border:2px solid gray"> </hr>

## Table of contents
* [Technologies](#technologies)
* [Project files description](#project-files-description)
* [Getting started](#getting-started)


<hr style="border:2px solid gray"> </hr>
	
## Technologies
Project is created with:
* python version: 3.6
* MongoDB

<hr style="border:2px solid gray"> </hr>

## Project files description

* app.py - Flask code for calling the scrapper function
* scraper.py  - Core file to scrape news websites
* db.py - MongoDB database for storing the scarpped data
* utils.py - 
* scheduler.py - Scheduling Heroku to run at regular intervals of time
* Procfile  - Commands to init Heroku platform
* requirements.txt - Library requirments 


<hr style="border:2px solid gray"> </hr>

## Getting-started
This project can be accessed by using following setup

**Request format**
```
$ Import requests
$ url = "http://www.newsemble.ml/news/"
$ requests.get(url).json()

```

**Response format**
```
{   ‘link’      :  ‘Source_link’,
    ‘content’   :  ‘Content_text’,    
    ‘source’    :  ‘News_source’,
    ‘title’     :  ‘Headline text’, 
    ‘time       :  ‘Article release time and date’  
 }

```
**Sample output**

![image](https://user-images.githubusercontent.com/52444089/125032819-1f5b3580-e0ac-11eb-9662-efa79dc0e099.png)

## Authors
