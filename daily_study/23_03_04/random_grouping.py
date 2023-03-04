# %%
import pandas as pd
import random as rd

# %%
    
class random_group:
    def __init__(self):
        self.members = ['김성훈', '장마가', '이장국', '김상민', '김동우',
           '이소정', '김도형', '한수아', '이혜원', '김준수',
           '신지은', '김현아', '강서연', '이아름',
           '신호림', '임도영', '정도', '석은수', '손지현',
           '김한림', '우광원', '하주리', '김수진', '서홍렬']
        rd.shuffle(self.members)    
        self.group = [[] for i in range(5)]
        self.random_grouping()
        self.printing_group()
        
    def random_grouping(self):
        j = 0
        for _ in range(len(self.members)):
            self.group[j].append(self.members.pop())
            if len(self.group[j]) == 5:
                j += 1
            elif len(self.members) == 0:
                break
    def printing_group(self):
        for i in range(len(self.group)):
            print(f'{i+1}조 '+' '.join(self.group[i]))           

a = random_group()



# %%
