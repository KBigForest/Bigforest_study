line1 = input()
line1
num = []
plusminus = []
for i in line1:
    if i == '+' or i == '-' :
        plusminus.append(i)
    else:
        num.append(i)
