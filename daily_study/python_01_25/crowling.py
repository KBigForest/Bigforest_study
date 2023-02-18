from urllib.request import urlopen
html = urlopen('https://www.daangn.com/hot_articles')
print(type(html))
print(html.read())

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(),	'html.parser')
print(bs)
print(bs.title)

print(bs.h1)
print(bs.div)

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try: 
    html = urlopen('http://www.pythonscraping.com/pages/error.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It worked!')
    

# 존재하지 않는 태그 접근
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read(),'html.parser')
        value = bs0bj.body.find(tag)
    except AttributeError as e:
        return None
    return value
tag = 'h2'
value = getTitle('http://www.pythonscraping.com/pages/page1.html', tag)
if value == None:
    print(f'{tag} could not be found')
else:
    print('value')
    
    
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.daangn.com/hot_articles')
bs = BeautifulSoup(html.read(),'html.parser')
print(bs.h1)
print(bs)





from bs4	import BeautifulSoup
soup	=	BeautifulSoup(html_example,	'html.parser')
print(soup.title)	#	<title>	태그 전체를 가져옴
print(soup.title.text)	#	<title>태그의 텍스트만 리턴
print(soup.title.get_text())	#	.text와 동일한 기능