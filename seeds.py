import json
from models2 import Author, Quote
import connect2

import requests
from bs4 import BeautifulSoup
page = 1
tags_ = []
quote_dict = {}
qoutes_json = []
author_dict = {}
author_json = []
fuln = []
avt_list = []


for page in range(11):
    url = 'https://quotes.toscrape.com/page/'+str(page)+'/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    author_body = soup.select("[href^='/author/']")
    
        
    tags = soup.find_all('div', class_='tags')

    for i in range(0, len(quotes)):        
        qt = {'quote': quotes[i].text}
        aut = {'author': authors[i].text}
        fuln.append(authors[i].text)
        avt_list_ = str(author_body[i]).strip("'<a href=>(about)</a>'")
        avt_list.append(avt_list_)
                    
        tagsforquote = tags[i].find_all('a', class_='tag')
        for tagforquote in tagsforquote:
            tags_.append(tagforquote.text)
        tgs = {"tags": tags_}   
        quote_dict.update(tgs)
        quote_dict.update(aut)
        quote_dict.update(qt)   
        qoutes_json.append(quote_dict)          
        tags_ = []      
      
for autor in avt_list: 
    #put()
   
    kilkist_ = len(avt_list)
    #print(kilkist_)
    
    lich = 1
    while lich != kilkist_ + 1:    
        lich = +1    
        kilkist = avt_list.count(autor)
        # print(autor)
        # print('hhhhhhh', kilkist)
        if kilkist > 1:
            index_ = avt_list.index(autor)
            #print(index_)            
            avt_list.pop(index_)
            #print(avt_list)
        break
print(avt_list)
for page_avt in avt_list:    
    
    page_av = page_avt[1:]
    page_a = page_av[:-1]    
    #print(page_a)
    url = 'https://quotes.toscrape.com'+page_a+'/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')    
    fullname = soup.find_all('h3', class_="author-title")
    born = soup.find_all('span', class_="author-born-date")
    born_loc = soup.find_all('span', class_="author-born-location")
    descript = soup.find_all('div', class_="author-description")
        
    for i in range(0, len(born)):        
        fulname = {'fullname: ' + fullname[i].text}
        bor_d = {'born_date: ' + born[i].text}
        bor_l = {'born_location: ' + born_loc[i].text}
        desc = {'description: ' + descript[i].text}
                
        # author_dict.update(fulname)
        # author_dict.update(bor_d)
        # author_dict.update(bor_l)
        # author_dict.update(desc)   
        # author_json.append(author_dict)  
    
        #print(author_json)        
     

#https://quotes.toscrape.com/author/Albert-Einstein/

# def load_authors():
#     with open("authors.json", 'r', encoding="utf-8") as file:
#         data_of_authors = json.load(file)
#         for author in data_of_authors:
#             auth = Author(fullname=author.get("fullname"),
#                          born_date=author.get("born_date"),
#                          born_location=author.get("born_location"),
#                          description=author.get("description"))
#             auth .save()
#     with open("qoutes.json", 'r', encoding="utf-8") as file:
#         data_of_quotes = json.load(file)
#         for quote_ in data_of_quotes:
#             quot = Quote(author_id=quote_.get("author_id"),
#                          quote=quote_.get("quote"),
#                          tags=quote_.get("tags"))
#             quot.save()    
            
            
# def save_data_from_form(data):
#     data_dict_1 = {}  
#     data_parse = urllib.parse.unquote_plus(data.decode())    
#     data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}   
#     with open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json', 'r') as fil:
#         data_dict_1 = json.load(fil)                          
#     data_dict_1.update({str(datetime.datetime.now()): data_dict})
#     with open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json', 'w', encoding='utf-8') as fil:
#         json.dump(data_dict_1, fil)
            
# if __name__ == '__main__':        
#     load_authors()
