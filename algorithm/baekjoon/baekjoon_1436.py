import sys
doom_num = []
num = int(input())
i = 0
count = 0
while True:
    if '666' in str(i):
        doom_num.append(int(i))
        count += 1        
    if count > num:
        break
    i += 1
print(doom_num[num-1])
