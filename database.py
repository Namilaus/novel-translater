from pymongo import MongoClient

class database:
    def __init__(self,url):
        self.url = url


    def connectToClient(self):
        client = MongoClient(self.url)
        
        return client['books']

    def connectToCollection(self):
        db = connectToClient()
        collection = db['translated_books']


