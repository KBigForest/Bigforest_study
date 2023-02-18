# 커피 자판기 프로그램 2016111032 경영학부 김한림
# ================================
# 기능1.  화면상에 메뉴를 출력하고 종료시 까지 반복
# - 1. 블랙커피, 2: 프림커피, 3: 설탕프림 커피, 4: 재고현황, 5: 종료
# - 커피 가격은 모두 300원으로 동일함
# 초기 자판기 상황 
# 자판기 동전 10,000원 100원짜리 100개 보유 중
# 물 1000ML
# 커피: 500g, 프림: 500g, 설탕: 500g, 종이컵 30개
# 블랙커피: 커피 30g + 물 100ml
# 프림커피: 커피 15g + 프림 15g + 물 100ml
# 설탕커피: 커피 10g + 프림 10g + 설탕 10g + 물 100ml
# 커피 재고량, 프림 재고량, 설탕 재고량, 컵 재고량, 잔여 물용량 출력
# - 잔돈 현황 출력 (입출금 관리)
# 
# ========================================
# 1. try/except로 동전말고는 딴거 투입 못하게 한다.
# 2. 만약 돈이 300원이 안되면 프로그램 종료
# 3. 그다음에서야 메뉴가 출력되게 한다.
# 4. 각 메뉴에 따라 다른 양의 재료가 소진되고 돈도 소진되게 한다.
# 5. 만약 잔돈이 남게 되면 다시 메뉴로 올린다.
# ========================================

class vanding_machine:
    #동전투입으로 바로 시작하게 하기
    def __init__(self):
        self.choice = 0
        self.changes = 10000
        self.water = 1000
        self.coffee = 500
        self.creamer = 500
        self.sugar = 500
        self.cup = 30
        try:
            self.input_money = int(input('동전을 투입하세요 : '))
   
        except:
            print('돈을 넣으셔야죠!!')
            self.__init__()
        
        if self.input_money < 300:
            print(f'돈이 부족합니다. 당신이 넣은돈은 겨우 이거밖에 안돼... {self.input_money}원')
            print('-'*20)
            print('커피 자판기의 동작을 종료합니다.')
            print('-'*20)
            return
        else:
            self.menu()
            
    def menu(self):
        while True:
            print('-'*20)
            print('        커피 자판기(300원)        ')
            print('1. 블랙커피')
            print('2. 프림커피')
            print('3. 설탕 프림 커피')
            print('4. 재고 현황')
            print('5. 종료')
            self.choice = input('메뉴를 선택하세요: ') 
            if self.choice in ['1']:
                print('-'*20)
                self.changes += 300
                self.input_money -= 300
                self.coffee -= 30
                self.water -= 100
                self.cup -= 1
                self.deplete()
                print(f'맛있는 블랙커피 대령이오~ 잔액: {self.input_money}')
            elif self.choice in ['2']:    
                print('-'*20)
                self.changes += 300
                self.input_money -= 300
                self.coffee -= 15
                self.creamer -= 15
                self.water -=100
                self.cup -= 1
                self.deplete()
                print(f'맛있는 프림커피 대령이오~ 잔액: {self.input_money}')
            elif self.choice in ['3']:    
                print('-'*20)
                self.changes += 300
                self.input_money -= 300
                self.coffee -= 10
                self.creamer -= 10
                self.sugar -= 10
                self.water -=100
                self.cup -= 1
                self.deplete()
                print(f'맛있는 설탕 프림 커피 대령이오~ 잔액: {self.input_money}')
            elif self.choice in ['4']:    
                print('-'*20)
                print('재고 현황')
                print(f'커피: {self.coffee}g, 프림: {self.creamer}g, 설탕: {self.sugar}g\n물: {self.water}ml, 종이컵 {self.cup}개\n자판기남은 돈: {self.changes}, 잔돈: {self.input_money}')
            elif self.choice in ['5']:    
                print('-'*20)
                print('자판기 종료!')
                return 0
            else:
                print('-'*20)
                print('제발 좀 버튼 눌러주세요...')
                continue
            
    def deplete(self):
        if self.water < 0:
            print('물이 부족해요...잘가요...')
            quit()
        elif self.coffee < 0:
            print('커피가루가 부족해요...잘가요...')
            quit()
        elif self.creamer < 0:
            print('프림이 부족해요...잘가요...')
            quit()
        elif self.cup < 0:
            print('컵이 없네요...잘가요...')
            quit()
        elif self.sugar < 0:
            print('설탕이 부족해요...잘가요...')
            quit()
        elif self.changes < 300:
            if self.input_money <= self.changes: 
                pass
            else:
                print('거스름돈 없네요. 잘가요...')
                quit()
        elif self.input_money < 0:
            print('잔액이 부족합니다. 잘가요...')
            quit()
        else:
            pass
a = vanding_machine()

