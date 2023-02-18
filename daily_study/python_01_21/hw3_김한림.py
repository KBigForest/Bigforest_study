# =====================================
# 알파벳 빈도수 그래프 출력
# 파일을 읽고 각 알파벳 소문자, 대문자 빈도수를 따로 계산 숫자랑 마침표는 다른 문자는 계싼 X
#
#  isalpha(),	isdigit(),	isspace()등 활용
# - str.islower():	문자열이 소문자이면 True
# - str.isupper():	문자열이 대문자이면 True


# 내가 구현해야 하는 것
# 1. 일단 안에 있는 내용을 가져오고
# 2. 해당 파일에 들어가는 알파벳이 있을 때
# 3. 대문자와 소문자 딕셔너리 생성하고
# 4. 해당 알파벳의 value값이 1씩 증가하는 기능구현
# 5. for i in str(file내용):
#   is alpha:
#       elif str.islower(i)==True:
#           소문자 딕셔너리 KEY i에 해당하는 value+1
#       elif str.isupper(i) == True:
#       대문자 딕셔너리 KEY i에 해당하는 value+1
#   elif isdigit():
#       pass
#   elif isspace():
#       pass
# 
# print('대문자: ')
# print(대문자 딕셔너리)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class alpha:
    def __init__(self):
        # 1. 파일 이름 입력해서 일단 안에 있는 내용을 가져오고
        self.upper_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0,'I':0,'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
        self.lower_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
        self.index_count = 0
        self.index_Count = 0
        #파일읽기
        self.read_file()
        #counting alpha~
        self.decision()
        #key값 순서대로 정렬
        self.upper_dict = dict(sorted(self.upper_dict.items(), key=lambda x: x[1], reverse=True))
        self.lower_dict = dict(sorted(self.lower_dict.items(), key=lambda x: x[1], reverse=True))
        #value가 0인거 제외
        self.upper_dict = {key: value for key, value in self.upper_dict.items() if value != 0}
        self.lower_dict = {key: value for key, value in self.lower_dict.items() if value != 0}
        #index 생성을 위한 count
        for i in self.upper_dict.values():
            if i > 0:
                self.index_Count += 1
        for i in self.lower_dict.values():
            if i > 0:
                self.index_count += 1
        #출력
        print('대문자')
        print(self.upper_dict)
            
        print('소문자')
        print(self.lower_dict)
        self.Index = np.arange(self.index_Count)
        self.index = np.arange(self.index_count)
        #그래프화
        self.graph_mat1()
        
        
    def read_file(self):
        try:
            self.file_name = input('Input file name : ')
            fp = open(self.file_name, mode = 'r', encoding='utf-8')
            self.allContents = fp.read()
            fp.close()
        except:
            print('없는 파일입니다.')
            self.read_file() 
            
    def decision(self):
        for i in self.allContents:
            if i.isalpha() == True:
                if str.islower(i)==True:
                    self.lower_dict[i] += 1
                    # 소문자 딕셔너리 KEY i에 해당하는 value+1
                elif str.isupper(i) == True:
                    self.upper_dict[i] += 1
                    # 대문자 딕셔너리 KEY i에 해당하는 value+1
            elif i.isdigit():
                    pass
            elif i.isspace():
                    pass
    
    def graph_mat1(self):
        plt.subplot(1,2,1)
        plt.rc("font", family='Malgun Gothic') 
        plt.bar(self.Index, self.upper_dict.values(), color = 'blue')
        plt.xlabel('Alphabet')
        plt.ylabel('Count')
        plt.title('대문자 개수')
        plt.xticks(self.Index,self.upper_dict.keys())
        
        plt.subplot(1,2,2)
        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.bar(self.index, self.lower_dict.values(), color = 'blue')
        plt.xlabel('Alphabet')
        plt.ylabel('Count')
        plt.title('소문자 개수') 
        plt.xticks(self.index,self.lower_dict.keys())
        plt.show()   
        
a = alpha()
