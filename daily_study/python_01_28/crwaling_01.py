from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.daangn.com/hot_articles')
print(type(html))
html.read()

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)
print(bs.h1.text)

from bs4 import BeautifulSoup
tr = '''
<table>
<tr class="passed a b c" id="row1 example"><td>t1</td></tr>
<tr class="failed" id="row2"><td>t2</td></tr>
</table>'''
x= []
table = BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr'):
    x.append(row['class'][0])
print(x)

html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BeautifulSoup 활용</title>
</head>
<body>
<h1 id="heading">Heading	1</h1>
<p>Paragraph</p>
<span	class="red">BeautifulSoup Library	Examples!</span>
<div	id="link">
<a	class="external_link"	href="www.google.com">google</a>
<div	id="class1">
<p	id="first">class1's first paragraph</p>
<a class="external_link"	href="www.naver.com">naver</a>
<p	id="second">class1's second paragraph</p>
<a	class="internal_link"	href="/pages/page1.html">Page1</a>
<p	id="third">class1's thirdparagraph</p>
</div>
</div>
<div	id="text_id2">
Example	page
<p>g</p>
</div>
<h1	id="footer">Footer</h1>
</body>
</html>'''

soup = BeautifulSoup(html_example,'html.parser')
a = soup.find_all('div')
for i in a:
    print(i.text)
    
a = soup.find_all('a',{'class':['external_link','internal_link']})
for i in a:
    print('url: {0}, domain: {1}'.format(i['href'], i.get_text()))
    
footer = soup.select_one('#footer')
print(footer.text)