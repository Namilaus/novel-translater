import requests
from bs4 import BeautifulSoup

def source(url):
    resContent = requests.get(url) # https://www.69shu.com/txt/1464/6929496
    return resContent.content

def parser(sourceCode,url):
    soup = BeautifulSoup(sourceCode,'html.parser')
    content = soup.find("div",{"class":"txtnav"})
    if content is None:
        return None

    return content.getText()


def getContent(url)->str:
    return parser(source(url),url)

def getBookNameUrl(url)->str:
    # in 69shu its not always the same but mostly so
    url = url[:-8]
    url = list(url)
    #url.insert(26, 'C')
    url.insert(31,'.htm')
    url.pop()
    bookurl = ""
    for el in url:
        bookurl+=el

    return bookurl

def getbookNameUrl2(url)->str:
    # another one
    url = url[:-8]
    url = list(url)
    url.insert(26, 'C')
    url.insert(31,'.htm')
    bookurl = ""
    for el in url:
        bookurl+=el

    return bookurl

def getBooksName(url)->str:
    url = getBookNameUrl(url)
    source = requests.get(url)
    soup = BeautifulSoup(source.content,'html.parser')
    name = soup.find("div",{"class":"booknav2"}).h1
    if name is None:
        url = getbookNameUrl2(url)  
        source = requests.get(url)
        soup = BeautifulSoup(source.content,'html.parser')
        name = soup.find("div",{"class":"booknav2"}).h1
    return name.getText()

def dynamicUrlEasy(url,length)->str:
    array = list()
    array.append(url)
    for i in range(1,length+1):
        url1 = url.split('/')
        number = int(url1[-1]) + i
    
        url1.pop(-1)
        url1.insert(6,str(number))
        url1.insert(1,'//')
        url1.insert(4,'/')
        url1.insert(6,'/')
        url1.insert(8,'/')
    
        realUrl = ''.join(url1)
        array.append(realUrl)

    return array;



#url = dynamicUrl('https://www.69shu.com/txt/1464/6929496', 10)
#print(url[-1])
#url = 'https://www.69shu.com/txt/1464/6929496'
#print(getBooksName(url))
