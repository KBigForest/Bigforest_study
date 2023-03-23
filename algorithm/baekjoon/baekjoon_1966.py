Num = int(input())
for i in range(Num):
    S, index = map(int, input().split())
    Importance = list(input().split())
    Importance = [int(i) for i in Importance]
    target = Importance[index]
    index_list = [0 for _ in range(S)]
    index_list[index] = 1
    index_list = list(index_list)
    target_index_list = []
    total_list = []

    while len(Importance) > 0:
        if Importance[0] == max(Importance):
            a = Importance.pop(0)
            total_list.append(a)
            b = index_list.pop(0)
            target_index_list.append(b)
        else:
            a = Importance.pop(0)
            Importance.append(a)
            b = index_list.pop(0)
            index_list.append(b)
    print(target_index_list.index(1.0)+1)

