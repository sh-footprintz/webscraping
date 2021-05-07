'''
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
'''

'''
from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.h1)
    print(bsObj.head)
'''
