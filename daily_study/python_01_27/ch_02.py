from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')
table_tag = soup.find('table', {'id':'giftList'})
for child in table_tag.children:
    print(child)
    
desc = soup.find('table', {'id':'giftList'}).descendants
print('descendants 개수: ', len(list(desc)))
for child in soup.find('table', {'id':'giftList'}).descendants:
    print(child)
    

#형제들을 찾아보자
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

# for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
#     print(sibling)

for sibling in  soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
    
for sibling in soup.find('tr',{'id':'gift2'}).previous_siblings:
    print(sibling)
    
style_tag = soup.style
print(style_tag.parent)

img1 = soup.find('img',{'src':'../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.text
print(text)


#정규식의 사용
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple','I like apple!'))

p = re.compile('[a-z0-9]+')
result = p.findall('I like apple 123')
print(result)

tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})')
m = tel_checker.match('02-123-4567')
m.group(1)

cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')
print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678').group(3))
