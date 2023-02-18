
html_example ='''
<!DOCTYPE html>
<html lang='en'><head><meta charset="UTF-8"><meta ame="viewport"	content="width=device-width, initial-scale=1.0"><title>BeautifulSoup 활용</title></head>
<body>
    <h1 id='heading'>Heading 1</h1>
    <p>Paragraph</p>
    <span class='red'>BeautifulSoup Library	Examples!</span>
    <div id='link'>
        <a class="external_link" href="www.google.com">google</a>
        <div id='class1'>
            <p id='first'>class1's first paragraph</p>
            <a class='external_link' href='www.naver.com'>naver</a>
            <p id='second'>class1's second paragraph</p>
            <a class='internal_link' href='/pages/page1.html'>Page1</a>
            <p id='third'>class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example	page
        <p>g</p>
    </div>
        <h1	id='footer'>Footer</h1>
    </body>
</html>'''

from bs4	import BeautifulSoup
soup	=	BeautifulSoup(html_example,	'html.parser')
print(soup.title)	#	<title>	태그 전체를 가져옴
print(soup.title.text)	#	<title>태그의 텍스트만 리턴
print(soup.title.get_text())	#	.text와 동일한 기능

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example,	'html.parser')
print(soup.find('div'))
div_text = soup.find('div',{'id':'text_id2'})
print(soup.find('div', {'id':'text_id2'}))
print(div_text.text)

href_link = soup.find('a',{'class':'internal_link'})
#동일함
href_link = soup.find('a', class_='internal_link')

print(href_link.text)
print('href_link.attrs: ', href_link.attrs)
print('href_link.attrs: ', href_link.attrs.values())
values = list(href_link.attrs.values())
print('values[0]: {0}, values[1]: {1}'.format(values[0],values[1]))
href_link['class']


tr = '''
<table>
<tr	class="passed	a	b	c"	id="row1	example"><td>t1</td></tr>
<tr	class="failed"	id="row2"><td>t2</td></tr>
</table>'''
table =	BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr'):
    print(row.attrs)


herf_value = soup.find(attrs={'href':'www.google.com'})
print(herf_value)
print(herf_value['href'])
print(herf_value.get_text())

span_tag = soup.find('span')
print('span tag:', span_tag)
print('attrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text',span_tag.text)

from bs4	import BeautifulSoup
html_example ='''
<!DOCTYPE html>
<html lang='en'><head><meta charset="UTF-8"><meta ame="viewport"	content="width=device-width, initial-scale=1.0"><title>BeautifulSoup 활용</title></head>
<body>
    <h1 id='heading'>Heading 1</h1>
    <p>Paragraph</p>
    <span class='red'>BeautifulSoup Library	Examples!</span>
    <div id='link'>
        <a class="external_link" href="www.google.com">google</a>
        <div id='class1'>
            <p id='first'>class1's first paragraph</p>
            <a class='external_link' href='www.naver.com'>naver</a>
            <p id='second'>class1's second paragraph</p>
            <a class='internal_link' href='/pages/page1.html'>Page1</a>
            <p id='third'>class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example	page
        <p>g</p>
    </div>
        <h1	id='footer'>Footer</h1>
    </body>
</html>'''
soup =	BeautifulSoup(html_example,	'html.parser')
# 전체 div 태그를 모두 검색 (리스트 형태로 반환)
div_tags =	soup.find_all('div')	
print('div_tags length:	',	len(div_tags))
for div in div_tags:
    print('-----------------------------------------------')
    # print(div)
    print(div.text.replace('\n',' '))    
    
links = soup.find_all('a')
for alink in links:
    print(alink)
    print('url:{0}, text:{1}'.format(alink['href'],alink.get_text()))
    print()
    
link_tags = soup.find_all('a', {'class':['external_link','internal_link']})
print(link_tags)

p_tags = soup.find_all('p',{'id':['first', 'third']})
for p in p_tags:
    print(p)
    
head = soup.select_one('head')
print(head)

h1 =	soup.select_one('h1')	#	첫 번째 <h1>태그 선택
print(h1)
from bs4 import BeautifulSoup
soup =	BeautifulSoup(html_example,	'html.parser')
head =	soup.select_one('head')
print(head)

footer = soup.select_one('h1#footer')
print(footer)

class_link = soup.select_one('a.internal_link')
print(class_link)
print(class_link.text)
print(class_link['href'])

link1 = soup.select_one('div#link > a.external_link')
print(link1)

# 모든 url 링크 검색
url_links = soup.select('a')
for link in url_links:
    print(link['href'])

link_find = soup.find('div', {'id':'link'})
external_link = link_find.find('a', {'class':'external_link'})
print(external_link)
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.text)

div_urls = soup.select('div#class1 > a')
print(div_urls)
print(div_urls[0]['href'])

h1 = soup.select('#heading, #footer')
print(h1)
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)

national_anthem = '''
<!DOCTYPE html>
<html lang="en">
<head>
<title>애국가</title>
</head>
<body>
<div>
<p id="title">애국가</p>
<p class="content">
동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br
>
무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br
>
</p>
<p class="content">
남산 위에
저 소나무 철갑을 두른
듯 바람서리 불변함은 우리 기상일세.<br
>
무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br
>
</p>
<p class="content">
가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br
>
무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br
>
</p>
<p class="content"> 이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br
>
무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br
>
</p>
</div>
</body>
</html>'''
    soup = BeautifulSoup(national_anthem, 'html.parser')
    print(soup.select_one('p#title').text)

    contents = soup.select('p.content')
    for content in contents:
        print(content.text)