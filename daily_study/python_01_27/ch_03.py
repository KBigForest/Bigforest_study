from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

from urllib.request import urlopen
from bs4 import BeautifulSoup
import random as rd
import re

rd.seed(None) #Python3.9 이상 
def getlinks(articleUrl):
    html = urlopen('https://en.wikipedia.org'+articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    bodyContent = bs.find('div', {'id': 'bodyContent'})
    wikiUrl = bodyContent.find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))
    return wikiUrl

links = getlinks('/wiki/Kevin_Bacon')
print('links 길이: ', len(links))
while(len(links)) > 0:
    newArticle = links[rd.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getlinks(newArticle)
    
    
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
count = 0
def getLinks(pageUrl):
    global count
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            count += 1
            print('[{0}]: {1}'.format(count, newPage))
            pages.add(newPage)
            getLinks(newPage)
    
getLinks('')
        

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
count = 0
def getLinks(pageUrl):
    global count
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.text)
        print(bs.find(id='mw-content-text').find('p'))
        print(bs.find(id='ca-edit').find('span').find('a').attr['href'])
    except AttributeError:
        print('this page is missing somethong Countinuing')
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            count += 1
            print('[{0}]: {1}'.format(count, newPage))
            pages.add(newPage)
            getLinks(newPage)
    
getLinks('')
    
    
from urllib.parse import urlparse

urlString1 = 'https://shopping.naver.com/home/p/index.naver'

url = urlparse(urlString1)
print(url.scheme)
print(url.netloc)
print(url.path)


from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(None)
#	웹 페이지에서 발견된 내부 링크를 모두 목록으로 만듬
def getInternalLinks(bs, includeUrl):
    includeUrl =	'{}://{}'.format(urlparse(includeUrl).scheme,	urlparse(includeUrl).netloc)
    internalLinks =	[]
    #	"/"로 시작하는 링크를 모두 찾음
    for link	in bs.find_all('a',	href=re.compile('^(/|.*' +	includeUrl +	')')):
        if link.attrs['href']	is not None:
            if link.attrs['href']	not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl +	link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks
def getExternalLinks(bs, excludeUrl):
    externalLinks =	[]
    #	현재 URL을 포함하지 않으면서 http나 www로 시작하는 링크를 모두 찾음
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href']	is not None:
            if link.attrs['href']	not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
def getRandomExternalLink(startingPage):
    try:
        html	=	urlopen(startingPage)
        bs	=	BeautifulSoup(html,	'html.parser')
        externalLinks =	getExternalLinks(bs, urlparse(startingPage).netloc)
        if len(externalLinks)	==	0:	#	외부 링크가 없으면 내부 링크 검색
            print('No external links, looking around the site for one')
            domain	=	'{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
            internalLinks =	getInternalLinks(bs,	domain)
            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)	- 1)])
        else:	#	랜덤하게 외부 링크 선택
            return externalLinks[random.randint(0,	len(externalLinks)	- 1)]
    except Exception as e:
        print('Exception 발생:', e)
        
def followExternalOnly(startingSite):
    externalLink =	getRandomExternalLink(startingSite)
    print('Random external link is:	{}'.format(externalLink))
    followExternalOnly(externalLink)
followExternalOnly('http://oreilly.com')