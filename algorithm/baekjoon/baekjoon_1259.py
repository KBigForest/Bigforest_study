while True:
    num = input()
    if len(num)% 2 == 0:
        front = num[:int(len(num)/2)]
        back = num[int(len(num)/2):][::-1]
        if front == back:
            print("yes")
        else:
            print("no")
    elif num == '0':
        break
    else:
        front = num[:int(len(num)/2)]
        back = num[int(len(num)/2)+1:][::-1]
        if front == back:
            print("yes")
        else:
            print("no")
    
