import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

'''
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
'''

'''
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.h1)
    print(bsObj.head)
'''

'''
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    return title

title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
'''

'''
url = "http://pythonscraping.com/pages/warandpeace.html"
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

greenList = bsObj.findAll("span", {"class":"green"})
for name in greenList:
    print(name.get_text())

print(bsObj.div.span)
'''

url = "http://pythonscraping.com/pages/page3.html"
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

#for child in bsObj.find("table", {"id":"giftList"}).children:
#    print(child)

#for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
#    print(sibling)

#print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

#images =  bsObj.findAll("img", {"src":re.compile("\.\.\/img/gifts/img.*\.jpg")})
#for image in images:
#    print(image["src"])

print(bsObj.findAll(lambda tag: len(tag.attrs)==2))