from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Y9DSKHZBw7c'
html = urlopen(url)
def	scraping_use_find(html):
    soup = BeautifulSoup(html, 'html.parser')
    pn = soup.find_all('p',{'class':'period-name'})
    sd = soup.find_all('p',{'class':'short-desc'})
    tt = soup.find_all('p',{'class':['temp temp-low','temp temp-high']})
    img = soup.find_all('img',{'class':'forecast-icon'})
    print('National Weather Service Scraping')
    print('----------------------------------')
    print('[find 함수 사용]')
    print('총 tomestone-container 검색 개수: {0}'.format(len(pn)))
    print('--------------------------------------------------------------------------------')
    for i in range(0,9):
        print('[Period]: {0}'.format(pn[i].text))
        print('[Short desc]: {0}'.format(sd[i].text))	
        print('[Temperature]: {0}'.format(tt[i].text))
        print('[Image desc]: {0}'.format(img[i]['title']))
        print('--------------------------------------------------------------------------------')
        	
scraping_use_find(html)

url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Y9DSKHZBw7c'
html = urlopen(url)
def	scraping_use_select(html):
    soup = BeautifulSoup(html, 'html.parser')

    pn = soup.select('p.period-name')
    sd = soup.select('p.short-desc')
    tt = soup.select('p.temp')
    img = soup.select('img.forecast-icon')
    
    print('National Weather Service Scraping')
    print('----------------------------------')
    print('[find 함수 사용]')
    print('총 tomestone-container 검색 개수: {0}'.format(len(pn)))
    print('--------------------------------------------------------------------------------')
    for i in range(0,9):
        print('[Period]: {0}'.format(pn[i].text))
        print('[Short desc]: {0}'.format(sd[i].text))	
        print('[Temperature]: {0}'.format(tt[i].text))
        print('[Image desc]: {0}'.format(img[i]['title']))
        print('--------------------------------------------------------------------------------')
        	
scraping_use_select(html)