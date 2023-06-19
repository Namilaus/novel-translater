import asyncio
from pymongo import MongoClient
from content import getBooksName,dynamicUrl,getContent
from translater import translatedText,isFinish

class database:
    def __init__(self,dbUrl,bookUrl,booklenght):
        self.dbUrl = dbUrl
        self.bookUrl = bookUrl
        self.booklenght = booklenght + 1

        

    async def connectToCollection(self):
        
        def connectToClient():
            client = MongoClient(self.dbUrl)
        
            return client['books']
        
        db = connectToClient()
        collection = db['translated_books']
        booksName = getBooksName(self.bookUrl)
        booksName = await translatedText(booksName)
        urls = dynamicUrl(self.bookUrl, self.booklenght);
        for element in urls:
            novel_content = getContent(element)
            novel_content = await translatedText(novel_content)
            data = {
                     "name":booksName,
                     "content":novel_content
                        }
            
            collection.insert_one(data)


url = 'https://www.69shu.com/txt/1464/6929496'
dburl = ''

test = database(dburl, url, 10)
asyncio.run(test.connectToCollection())


#TODO the google translater doesnt get from one ip multiple task at the same time, cause
# of that I got some error I tried to use await but it doesnt
# so I have lern more about await and do some test with google translaters API
