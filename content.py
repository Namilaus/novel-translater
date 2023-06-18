import requests
from bs4 import BeautifulSoup

def source(url):
    resContent = requests.get(url) # https://www.69shu.com/txt/1464/6929496
    return res.content

def parser(sourceCode):
    soup = BeautifulSoup(sourceCode,'html.parser')
    content = soup.find("div",{"class":"txtnav"})
    return content.getText()


def getContent(url)->str:
    return parser(source(url))

def getBookNameUrl(url)->str:
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
    return name.getText()

def dynamicUrl(url,length)->str:
    array = list()
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
