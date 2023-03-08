import sys
num = int(sys.stdin.readline())
full_list = []
for i in range(num):
    line = input()
    full_list.append(line)
full_list = list(set(full_list))
full_list.sort()
full_list.sort(key = lambda x: len(x))

for i in full_list:
    print(i)