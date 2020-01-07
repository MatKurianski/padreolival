import os
import pymongo
import dotenv

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

url = os.getenv('MONGO_DB_URL')
CLIENT = pymongo.MongoClient(url)
db = CLIENT.pecados
