# This for check the results of scrapping...
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['scrapyDB']

# Let's print 10 results from the both collections

for vacancy in db['superjob.ru'].find({})[:10]:
    pprint(vacancy)

for vacancy in db['hh.ru'].find({})[:10]:
    pprint(vacancy)
