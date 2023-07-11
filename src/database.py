from pymongo import MongoClient
from content import getBooksName,dynamicUrl,getContent
from translater import translatedText
import certifi

class database:
    def __init__(self,dbUrl,bookUrl,booklenght):
        self.dbUrl = dbUrl
        self.bookUrl = bookUrl
        self.booklenght = booklenght + 1

        

    def connectToCollection(self):
        
        def connectToClient():
            client = MongoClient(self.dbUrl,tlsCAFile=certifi.where())
        
            return client['books']
        
        db = connectToClient()
        collection = db['translated_books']
        booksName = getBooksName(self.bookUrl)
        booksName = translatedText(booksName)
        urls = dynamicUrl(self.bookUrl, self.booklenght);
        for element in urls:
            novel_content = getContent(element)
            novel_content = translatedText(novel_content)
            data = {
                    "name":booksName,
                     "content":novel_content
                        }
            
            collection.insert_one(data)


url = ''
dburl = ''

test = database(dburl, url, 100)
test.connectToCollection()


#TODO the google translater doesnt get from one ip multiple task at the same time, cause
# of that I got some error I tried to use await but it doesnt work
# so I have lern more about await and do some test with google translaters API


# it turns out it wasnt the problem google translater but from the database it had
# some problem with authentication so as soon as I found solution to that
# My code did work (actually note my code due to using so many packages...)

