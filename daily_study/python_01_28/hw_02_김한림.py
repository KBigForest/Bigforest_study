# ======================================
# 할리스 매장 정보확인 프로그램
# 메인메뉴
# 1~3번 이외의 입력은 다시 반복시키기
# 1. 현재 전체 매장 출력 및 저장
#   현재 매장의 정보를 가져와서 value리스트로 가져와서 append하고 데이터 프레임화 시켜서 csv화 하기
# 2. 매장 검색
#   - main입력 시 메인메뉴행 
#   - quit 입력시 종료
 

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
class search_hollys:
    store_info = []            
    
    def __init__(self):
        print('-'*50)
        print('안녕하세요 할리스 매장 현황 확인 프로그램입니다.')
        print('-'*50)
        self.hollys_choice()



    def hollys_choice(self):
        while True:
            print('1. 전체 매장 정보 확인 및 저장\n2. 도시 별 매장 검색\n3. 종료')
            try:
                f_num = int(input('메뉴선택: '))
            except:
                print('잘못된 입력입니다.')
                self.hollys_choice()
         
            if f_num == 1:
                print('현재 전체 매장 결과를 출력합하고 csv로 저장합니다.')
                self.all_store()
                self.save()
            elif f_num == 2:
                print('도시별 매장 검색입니다.')
            elif f_num == 3:
                break
            else:
                print('잘못된 입력입니다.')
                
    def all_store(self):
        store_num = 1
        for i in range(1,54):
            url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
            html = urlopen(url)
            soup = BeautifulSoup(html.read(),'html.parser')
            store = soup.select('tbody tr')
            for i in store:
                values = i.text.split('\n')
                print('[ {0}]: 매장이름: {1}, 지역: {2}, 주소: {3}, 전화번호: {4}'.format(store_num, values[3], values[2], values[5], values[9]))
                store_num += 1
                self.store_info.append([values[3], values[2], values[5], values[9]])
    def save(self):
        self.DF_store_info = pd.DataFrame(self.store_info, columns=['매장이름','위치(시/구)','주소','전화번호'])
        self.DF_store_info.to_csv('coffeestore_info.csv',encoding='utf-8')
a = search_hollys()