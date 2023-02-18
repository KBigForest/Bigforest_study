# 테니스공 FILO 프로그램
# 조건: 1차원 array사용
# class 구성:
# 1. 메뉴선택 while안에 try, except로 예외처리
# 2. 1번 선택 push함수 구성
#    이거는 아마 append하는 느낌으로
#    len이 아마 6개 이상일 경우는 해당 하는 함수 내에서 append시키지 않도록 예외처리
#    print('삐빅 꽉찼습니다.')
# 3. 2번 선택 pop함수 구성
#    len이 0인 경우, 안된다고 예외처리
# 4. 3번 선택 시 array를 출력만 해주면됨 개꿀
#       아님..len(array)의 개수가 0일때는 print('케이스가 비어 있습니다.')
# 5. 4번 선택 시 종료
import numpy as np

class tennis:
    a = np.array([])
    
    
    def __init__(self):    
        while True:
            print()
            print('------------------------------')
            print('1. 테니스 공 넣기')
            print('2. 테니스 공 꺼내기')
            print('3. 테니스 공 개수 출력')
            print('4. 종료')
            try:
                choice = int(input('메뉴를 선택하세요: '))                      
            except:
                print('잘못된 입력입니다.')
            if choice == 1:
                self.push()
                print(f'[공의 개수]: {self.a.size}')
                for i in range(0,len(self.a)):
                    print(self.a.astype('int32')[i], end = ' ')
                    
                        
            elif choice == 2:
                self.poppop()
                print(f'[공의 개수]: {self.a.size}')
                for i in range(0,len(self.a)):
                    print(self.a.astype('int32')[i], end = ' ')
                    
                
            elif choice == 3:
                if len(self.a) == 0:
                    print('케이스가 비어 있습니다.')
                else:
                    print(f'[공의 개수]: {self.a.size}')
                    for i in range(0,len(self.a)):
                        print(self.a.astype('int32')[i], end = ' ')
                    
            
            elif choice == 4:
                print('프로그램 종료')
                break
            else:
                print('잘못된 입력입니다.')  
    def push(self):
        if self.a.size < 5:
            ball = self.a.size+1
            self.a = np.append(self.a, np.array([ball]))
            self.a.astype('int32')
            self.a = np.sort(self.a)[::-1]
        elif self.a.size == 5:
            print('케이스가 꽉 차 있습니다.')
            
    def poppop(self):
        if self.a.size == 0:
            print('케이스가 비었습니다.')
        else:
            self.a = np.delete(self.a, 0)
            
a = tennis()