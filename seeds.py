import json
from models2 import Author, Quote
import connect2

def load_authors():
    with open("authors.json", 'r', encoding="utf-8") as file:
        data_of_authors = json.load(file)
        for author in data_of_authors:
            auth = Author(fullname=author.get("fullname"),
                         born_date=author.get("born_date"),
                         born_location=author.get("born_location"),
                         description=author.get("description"))
            auth .save()
    with open("qoutes.json", 'r', encoding="utf-8") as file:
        data_of_quotes = json.load(file)
        for quote_ in data_of_quotes:
            quot = Quote(author_id=quote_.get("author_id"),
                         quote=quote_.get("quote"),
                         tags=quote_.get("tags"))
            quot.save()    
            
            
def save_data_from_form(data):
    data_dict_1 = {}  
    data_parse = urllib.parse.unquote_plus(data.decode())    
    data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}   
    with open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json', 'r') as fil:
        data_dict_1 = json.load(fil)                          
    data_dict_1.update({str(datetime.datetime.now()): data_dict})
    with open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json', 'w', encoding='utf-8') as fil:
        json.dump(data_dict_1, fil)
            
if __name__ == '__main__':        
    load_authors()
