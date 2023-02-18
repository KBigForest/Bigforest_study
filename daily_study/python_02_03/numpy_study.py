import numpy as np
a = np.array([1,2,3])
a
a.shape
a.ndim
a.dtype
a.itemsize

a = np.array([1,2,3], dtype= 'int32')
b = np.array([4,5,6], dtype= 'int64')
a+b

import numpy as np
a= np.zeros((3,4))
print(a)
a= np.ones(10)
print(a)
b = np.eye(4)
print(b)

import numpy as np
import matplotlib.pyplot as plt
print(np.arange(3))
a = np.arange(0,10,2)
print(a)
plt.plot(a,'o')
plt.show()
x= '123'
x[0:0]

import numpy as np
scores = np.array([[99, 93, 60], [98, 82, 93], [93, 65, 81], [78, 82, 81]], dtype= 'int64')
mean_col = scores.mean(axis=0)
mean_row =	scores.mean(axis=1) # row단위 계산
print(mean_col)
print(mean_row.round(2))