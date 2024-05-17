import requests
from bs4 import BeautifulSoup
import json
from multiprocessing import connection
from datetime import datetime
import random
import sqlite3
import random

user_agent_list = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15', 
]

print("Search Keyword: ")
searchKeyword = input()      #Getting a keyword to scrap quotes
searchKeyword = searchKeyword.replace(" ","+")
result = []


#Quotes scraping for the first page of search result
def QuotesScraping():
    #Choosing an user agent randomly to avoid blocking from site
    user_agent = random.choice(user_agent_list) 
    headers = {'User-Agent': user_agent}
    
    #Accessing the site URL and its content
    site_url = "https://www.brainyquote.com/search_results?q="+searchKeyword+"&pg=1"
    webpage = requests.get(site_url, headers=headers)
    
    if webpage.status_code == 200:
      web = webpage.text
      soup = BeautifulSoup(web, "html.parser")
      
      #Finding the quotes with class and getting the desired data
      box = soup.findAll(class_='grid-item qb clearfix bqQt')     
      
      for item in box:
        quote = author = item.find(class_="b-qt").text.strip()
        author = item.find(class_="bq-aut").text
        quote_url = "https://www.brainyquote.com"+item.find(class_="b-qt")["href"]
        author_url = "https://www.brainyquote.com"+item.find(class_="bq-aut")["href"]
        object = {}
        object["Quote"] = quote
        object["Author"] = author
        object["Quote URL"] = quote_url
        object["Author URL"] = author_url
        result.append(object)
    else:
      print("The URL is not retrieved successfully", webpage.status_code)



#Calling Function To Scrap
QuotesScraping()

#Converting result dictionary to json format
final = json.dumps(result, indent=2)
print(final)

#Ensuring a unique id with randint & datetime combination
randomNumber = random.randint(1,1000)
id = int(datetime.now().microsecond)+randomNumber

#Creating a database connection with my DRF project database path 
connection = sqlite3.connect('Please Insert Your Database Path')
cursor = connection.cursor()

#Inserting scraped data to database
connection.execute('insert into scraper_scrap values(?,?,?)',[id,searchKeyword,final])
connection.commit()