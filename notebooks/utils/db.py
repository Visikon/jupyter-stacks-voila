# Import libraries
from pymongo import MongoClient

def dev():
    dev_client = MongoClient('localhost', 27017)
    return dev_client['vCoreDev']

def qa():
    qa_client = MongoClient('mongodb://db-core-qa:Jh1ihYmFDkkb65i9bEWSafzLJxFdkNcUYbcWpF0fh8YOS3tc7n4C5NRtauFNjrvpP11VdcJ04pYIQMwneKSLGg==@db-core-qa.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@db-core-qa@')
    return qa_client['admin']

def prod():
    prod_client = MongoClient('mongodb://visikoncore:lKBjBGmTCFGNQMS7Q9mM8OZbZs91AqyDpxHWmD13TJ28GFxpTcmHFoMYEfbcx5a8JU0BpoxDseawKJXj9yQSEQ==@visikoncore.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@visikoncore@')
    return prod_client['admin']

# Explore DB collections
# db.list_collection_names()
