list1 = []
list2 = []
except_list_index =[]
    
def gang(list1,list2,except_list_index):
    for i in range(1,len(list1)):
        if i == 1:
            print(list1[i-1] + list2[i])

        elif i in except_list_index:
            print('예외처리')
        else:
            print(list1[i])