"""
Authors: Rishabh Gupta (rg089), Vishal Singhania (vishalvvs)
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

class IndiaToday():
    @staticmethod
    def generate_dataset():
        data= []
        for i in range(3):
          url = "https://www.indiatoday.in/top-stories" + "?page=" + str(i)
          html = requests.get(url)
          soup = BeautifulSoup(html.text,"lxml")
          for i in soup.find_all(class_ = "catagory-listing"):
              news_url = 'https://www.indiatoday.in/'+i.a["href"]
              news_title, news_content, time = IndiaToday().get_content(news_url)
              if news_content == None or news_content == "":
                  continue
              article = {}
              article["link"] = news_url
              article["content"] = news_content
              article["source"] = "IT"
              article["title"] = news_title
              article["time"] = time
              data.append(article)
        return data
    
    @staticmethod
    def get_content(url):
        ar = requests.get(url)
        article = BeautifulSoup(ar.text,"lxml")
        title = article.find("h1").get_text()
        try:
          time = article.find("span", class_="update-data").text
          time = re.sub("Updated:|IST|AM|PM", "", time, flags=re.IGNORECASE).strip()
        #   time = datetime.strptime(time, "%B %d, %Y %H:%M")
        except:
          time = None
        if (article.find('div',{"class":"description"}) == None) or time==None:
            return None, None, None
        else:
            content = ""
            for para in article.find(class_ = "description").find_all("p")[:-3]:
                content+=para.get_text()
            return title,content,time

class TheHindu():
    @staticmethod
    def get_content(url):
        html = requests.get(url)
        article = BeautifulSoup(html.text,"lxml")
        content = "", time = ""
        for i in article.find_all("span", class_="blue-color ksl-time-stamp"):
            if i.find("none") is not None:
                time = i.get_text()
                time = re.sub("Updated:|IST|AM|PM", "", time, flags=re.IGNORECASE).strip()
                break
        # time = datetime.strptime(time, "%B %d, %Y %H:%M")
        paras = article.find_all("p")[1:-5]
        for para in paras:
            content+=para.get_text()
        return content, time
    
    @staticmethod
    def generate_dataset():
        url = "https://www.thehindu.com/trending/"
        html = requests.get(url)
        soup = BeautifulSoup(html.text,"lxml")        
        data = []
        
        for story in soup.find_all(class_ = "story-card-news"):
            news_title = story.get_text().split("\n")[6]
            content_url = story.find_all("a")[2].get('href')
            content, time = TheHindu.get_content(content_url)
            if content != "":
                article = {}
                article["link"] = content_url
                article["content"] = content
                article["source"] = "TH"
                article["title"] = news_title
                article["time"] = time
                data.append(article)
            else:
                continue
        return data

class TimesOfIndiaNews():

    @staticmethod
    def get_toi_links_titles():
        url = "https://timesofindia.indiatimes.com/news"
        data = requests.get(url).content
        soup = BeautifulSoup(data,"lxml")
        pages = len(soup.find("ul", class_ = "curpgcss").find_all("li"))
        page_data = [soup] + [BeautifulSoup(requests.get(url+f"/{page_num}").content, "lxml") for page_num in range(2, pages+1)]
        links_titles = []
        for page in page_data:
            ul = page.find('ul', {'class': 'cvs_wdt clearfix', "data-msid": "-2128958273"})
            links_titles += [("https://timesofindia.indiatimes.com" + li.find("a").get("href", ""), li.find("a").get("title", "")) for li in ul.find_all("li") if li.find("a").get("href", "").startswith("/")]
        return links_titles

    @staticmethod
    def get_toi_links_titles_old(div_class):
        url = "https://timesofindia.indiatimes.com/home/headlines"
        data = requests.get(url).content
        soup = BeautifulSoup(data,"lxml")
        ul = soup.find('div', {'class': div_class}).find('ul', {'class': 'clearfix'})
        links_titles = [("https://timesofindia.indiatimes.com" + li.find("a").get("href", ""), li.find("a").get("title", "")) for li in ul.find_all("li") if li.find("a").get("href", "").startswith("/")]
        return links_titles

    @staticmethod
    def get_toi_content(url):
        data = requests.get(url).content
        soup = BeautifulSoup(data,"lxml")
        div = soup.find("div", class_= "_3YYSt clearfix ")
        if div is None:
            div = soup.find("div", class_= "_3YYSt clearfix")
        if div is not None:
            time = soup.find("div", class_="yYIu- byline").find("span").text
            time = re.sub("Updated:|IST|AM|PM", "", time, flags=re.IGNORECASE).strip()
            # time = datetime.strptime(time, "%b %d, %Y, %H:%M")
            return "".join(list(div.strings)), time
        return None, None

    @staticmethod
    def generate_dataset():
        # link_titles = TimesOfIndiaNews.get_toi_links_titles("headlines-list") + TimesOfIndiaNews.get_toi_links_titles("top-newslist")
        link_titles = TimesOfIndiaNews.get_toi_links_titles()
        data = []
        for link, title in link_titles:
            article = {}
            content, time = TimesOfIndiaNews.get_toi_content(link)
            if content is not None:
                article["link"] = link
                article["title"] = title
                article["source"] = "TOI"
                article["content"] = content
                article["time"] = time
                data.append(article)
        return data

class NDTVNEWS():
    @staticmethod
    def generate_dataset():
        data= []
        url = "https://www.ndtv.com/top-stories"
        html = requests.get(url)
        soup = BeautifulSoup(html.text,"lxml")
        for i in soup.find_all("h2",{"class" : "newsHdng"}):
            news_title = i.get_text().strip()
            news_url = i.a["href"]
            news_content, time = NDTVNEWS().get_content(news_url)
            article = {}
            article["link"] = news_url
            article["content"] = news_content
            article["source"] = "NDTV"
            article["title"] = news_title
            article["time"] = time
            data.append(article)
        return data
    
    @staticmethod
    def get_content(url):
        ar = requests.get(url)
        article = BeautifulSoup(ar.text,"lxml")
        if article.find('div',{'id':"ins_storybody"}) == None:
            return None, None
        else:
            time = article.find("span", {"itemprop":"dateModified"}).text
            time = re.sub("Updated:|IST|AM|PM", "", time, flags=re.IGNORECASE).strip()
            # time = datetime.strptime(time, "%B %d, %Y %H:%M")
            content = ""
            for para in article.find('div',{'id':"ins_storybody"}).find_all("p"):
                content+=para.get_text()
            return content, time

class TheIndianExpress():
    
    @staticmethod
    def generate_dataset():
        data= []
        url = "https://indianexpress.com/section/india/"
        html = requests.get(url)
        soup = BeautifulSoup(html.text,"lxml")
        for i in soup.find_all(class_ = "title"):
            news_title = i.get_text()
            news_url = i.a["href"]
            news_content, time = TheIndianExpress().get_content(news_url) 
            if news_content is not None:
                article = {}
                article["link"] = news_url
                article["content"] = news_content.strip()
                article["source"] = "TIE"
                article["title"] = news_title.strip()
                article["time"] = time
                data.append(article)
            else:
                pass
        return data
    
    @staticmethod
    def get_content(url):
        ar = requests.get(url)
        article = BeautifulSoup(ar.text,"lxml")
        if article.find(id="pcl-full-content") == None:
            return None, None
        else:
            time = article.find("span", {"itemprop":"dateModified"}).text
            time = re.sub("Updated:|IST|AM|PM", "", time, flags=re.IGNORECASE).strip()
            # time = datetime.strptime(time, "%B %d, %Y %H:%M:%S")
            content = ""
            for para in article.find('div', id = "pcl-full-content").find_all("p"):
                content+=para.get_text()
            return content, time

                
class Data:
    @staticmethod
    def collect(source="all"):
        """
            Input : Ticker of News Site to Scraper, Default : The Indian Express
            Output: List of Dictionary of the scraped articles from the source site
        """

        d = {"toi":TimesOfIndiaNews,"tie":TheIndianExpress,"th":TheHindu,"it":IndiaToday,"ndtv":NDTVNEWS}
        if source in d:
            news = d[source].generate_dataset()
            return news
        elif source == "all":
            papers = [IndiaToday, TheHindu, TimesOfIndiaNews, NDTVNEWS, TheIndianExpress]
            articles = []
            for paper in papers:
                articles += paper.generate_dataset()
            return articles
        return None
