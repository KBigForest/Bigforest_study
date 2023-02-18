# datetime의 이해
import datetime as dt
x = dt.datetime(2016, 1, 3)
x= dt.datetime.today()
print(x)

x.strftime('%A %d %b %Y')

x = dt.date(2023, 2, 28)
y = dt.date(2023, 1, 15)
x-y
d = dt.timedelta(days=409)
d.total_seconds()

from dateutil.relativedelta import relativedelta

x = dt.datetime(2000,12,31)
y = relativedelta(months=12)
x-y


import time
time.sleep(5)
print(x)
##클래스의 이해
# 메서드 오버라이딩의 이해
# 부모에게 상속받은 같은 이름의 메서드를 다른방식으로 사용하는 것을 의미함
# 게임 캐릭터 코드에서 attacked 메서드도 오버라이딩을 하여 전사와 마법사가 공격을 받을 때 life 속성값이 다르게 감소하도록 한다.

class character:
    def __init__(self):
        self.life = 1000
    
    def attacked(self):
        self.life -= 10
        print(f'공격받았습니다.. 윽 생명력은 {self.life}' )
        
# 이 코드에서 super(자식클래스이름, self).__init()__ 부분은 부모 클래스의 초기화 생성자를 호출하는 부분이다.         
class warrior(character):
        def __init__(self):
             super(warrior, self).__init__()
             
        def attacked(self):
            self.life -= 20
            print(f'방어력이 약해서 더 아파요.. 생명력은 {self.life}')
            
a = warrior()
a.attacked()
a = character()
a.attacked()
