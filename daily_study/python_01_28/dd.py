from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

num=1
branch = list()
for i in range(1,54):
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
    html = urlopen(url)
    soup = BeautifulSoup(html.read(),'html.parser')
    table = soup.select_one('tbody')
    rows = table.select('tr')
    for row in rows:
        values = row.text.split('\n')
        print(f'[{num}]:매장이름:{values[3]}, 지역:{values[2]}, 주소:{values[5]}, 전화번호:{values[-2]}')
        branch.append([values[3],values[2],values[5],values[-2]])
        num+=1
    html.close()