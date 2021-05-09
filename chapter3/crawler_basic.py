from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

'''
url = "https://en.wikipedia.org/wiki/Kevin_Bacon"
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")
'''

'''
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''

'''
for link in bsObj.find("div", {"id":"bodyContent"}).\
        findAll("a", href=re.compile("^(/wiki/)((?!:).).*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''

'''
def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}). \
        findAll("a", href=re.compile("^(/wiki/)((?!:).).*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
'''

'''
pages = set()
def getLinks(articleUrl):
    global pages
    
    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
'''

'''
def getLinks(articleUrl):
    global pages

    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("---\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
'''
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []

    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")) :
        if link == None:
            return externalLinks

        if link.attrs['href'] is not None :
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])

    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])

    if len(externalLinks) == 0:
        pass
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startSite):
    externalLink = getRandomExternalLink(startSite)
    print("random external link : " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("https://en.wikipedia.org;")