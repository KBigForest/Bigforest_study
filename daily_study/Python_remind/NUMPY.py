import numpy as np
a =np.array([1,2,3,4])
a
type(a)
a.dtype
a.dtype([1.0])
#리스트는 곱셈시 해당 요소를 뒤에 그만큼 곱한 횟수만큼 추가해준다.
data = [0,1,2,3,4]
data * 2

a = np.array([1,2,3])
b = np.array([10,20,30])
a*2 +b

a==2
b > 10
(a == 2)&(b > 10)

c = np.array([[0,1,2], [3,4,5]])
len(c)
len(c[0])
np.array([[10,20,30,40],[50,60,70,80]])

# 3차원 배열만들기
d = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[11,12,13,14],[15,16,17,18],[19,20,21,22]]])
len(d)
len(d[0])
len(d[0][0])
a = np.array([1, 2, 3])
print(a.ndim)
print(a.shape)

c = np.array([[0, 1, 2], [3, 4, 5]])
print(c.ndim)
print(c.shape)

a = np.array([0,1,2,3,4,5,6,7,8,9])
idx = np.array([True, False, True, False, True, False, True, False, True, False])
a[idx]
a % 2 == 0
a[a % 2== 0]


a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8])
a[idx]



a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a
len(a)
len(a[0])
a[:,[True, False, False, True]]





x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
x[(x % 4 == 1) & (x % 3 ==0)]



