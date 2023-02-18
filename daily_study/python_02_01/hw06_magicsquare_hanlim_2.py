#마방진
#1. 각 입력되는 수(n)에 대한 2차원 배열을 만든다
#2. 2차원 배열에 해당하는 배열은 0으로 더미값을 준다.
#3. 마방진의 이동원리에 따라 이동을 시키고 해당 값에 대해서 값이 > 0 그동안은 계속 반복 시키면서 좌표를 이동시킨다.
#4. 값이 0인 경우 해당하는 count 수를 넣으면된당


class mabangjin:
    def __init__(self):
        try:
            self.num = int(input('홀수차 배열의 크기를 입력하세요: '))
        except:
            print('잘못된 입력입니다. 다시 입력하세요.')
            self.__init__()
        
        if self.num not in [3,5,7,9]:
            if self.num % 2 == 0:
                print('짝수를 입력하였습니다. 다시 입력하세요.')
                self.__init__()
            else:
                print('구현되지 않은 마방진입니다.\n다시 입력하세요.')
                self.__init__()
        else:
            print('시작')
            self.calculate()
    def calculate(self):    
        list1 = [[0 for i in range(self.num)] for i in range(self.num)]
        x = int(self.num / 2)
        y = 0
        list1 = [[0 for i in range(self.num)] for i in range(self.num)]
        list1[y][x] = 1
        for i in range(2,self.num*self.num+1):
            y -= 1
            x += 1
            if list1[y % self.num][x%self.num] != 0:
                y += 2 
                x -= 1
                list1[y % self.num][x % self.num] = i
            else:
                list1[y % self.num][x % self.num] = i
        for i in list1:
            for j in i:
                print(j, end = ' ')
            print()
a = mabangjin()
