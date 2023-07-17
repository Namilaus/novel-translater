from pymongo import MongoClient
from content import getBooksName,dynamicUrlEasy,getContent
from translater import translatedText
import certifi
from dynamicUrlhard import dynamicUrlHard

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
        print(self.bookUrl)
        booksName = getBooksName(self.bookUrl)
        booksName = translatedText(booksName)
        urls = dynamicUrlEasy(self.bookUrl, self.booklenght);
        lastUrl = ''
        IsNeeded = False
        newLength = 0
        for index,element in enumerate(urls):
            novel_content = getContent(element)
            if novel_content is None:
                lastUrl = urls[index-1]
                newLength  = self.booklenght - index
                self.booklenght = newLength
                IsNeeded = True
                break
            novel_content = translatedText(novel_content)
            data = {
                    "name":booksName,
                     "content":novel_content,
                     "url":element,
                     "easy":True
                        }
            
            collection.insert_one(data)
        if IsNeeded:
            urls = dynamicUrlHard(lastUrl, self.booklenght)
            for element in urls:
                novel_content = getContent(element)
                novel_content = translatedText(novel_content)
                data = {
                        "name":booksName,
                         "content":novel_content,
                         "url":element
                        }
            
                collection.insert_one(data)


url = 'https://www.69shu.com/txt/47115/31439983'
dburl = ''


test = database(dburl, url, 50)
test.connectToCollection()


#TODO the google translater doesnt get from one ip multiple task at the same time, cause
# of that I got some error I tried to use await but it doesnt work
# so I have lern more about await and do some test with google translaters API


# it turns out it wasnt google translaters problem but from the database it had
# some problem with authentication so as soon as I found solution to that
# My code did work (actually not my code due to using so many packages...)

