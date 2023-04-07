roof = int(input())
roof_list = []
for i in range(roof):
    N = int(input())
    roof_list.append(N)
roof_list = sorted(roof_list,reverse=False)

y = 0
for i in roof_list:
    x = i*roof
    roof -=1
    if y < x:
        y = x
    else: pass
print(y)