from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
market_info = []    
for i in range(0, 52):
    html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store=')
    soup = BeautifulSoup(html.read(), 'html.parser')
    market = soup.select_one('tbody > tr')
    market.append()