from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
query = quote('대구+날씨')
url = 'https://search.naver.com/search.naver?query=' + query
html = urlopen(url)

def deagu_weather(html):
    soup = BeautifulSoup(html, 'html.parser')
    taap = soup.find('h2',{'class':'title'})
    nowtemp = soup.find('div',{'class':'temperature_text'})
    weather_con = soup.find('span',{'class':'weather before_slash'})
    txt = soup.find_all('span',{'class':'txt'})
    dt_time = soup.find_all('dt',{'class':'time'})
    num = soup.find_all('span', {'class':'num'})
    time_weather = soup.select('dd.weather_box > i.wt_icon')
    
    print(f'현재 위치: {taap.text}')
    print(f'현재 온도: {nowtemp.text}')
    print(f'날씨 상태: {weather_con.text}')
    print(f'미세먼지 {txt[0].text}')
    print(f'초미세먼지 {txt[1].text}')
    print(f'자외선 {txt[2].text}')
    print(f'일출 {txt[3].text}')
    print('-----------------------')
    print('시간대별 날씨 및 온도')
    print('-----------------------')
    for t in range(0,72):
        print(f'{dt_time[t].text} {time_weather[t].text}  {num[t].text} ')
        
deagu_weather(html)