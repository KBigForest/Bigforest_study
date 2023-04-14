num1, num2 = map(str, input().split())
#max
num1 = num1.replace('5', '6')
num2 = num2.replace('5', '6')
maxnum = int(num1)+int(num2)

num1 = num1.replace('6', '5')
num2 = num2.replace('6', '5')
minnum = int(num1)+int(num2)
print(minnum, maxnum)