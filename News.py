#Make sure you have connection before using this
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def GetNews():
    url = "https://news.google.com/news/rss"
    client = urlopen(url)

    page = client.read()
    client.close()

    soup_page = soup(page, "xml")
    news_list = soup_page.findAll("item")


    for news in news_list:
      print(news.title) #Print title
      print("\n")
      print(news.link.text) #Print Link
      print("\n")


