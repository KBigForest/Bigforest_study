import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4],[1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

plt.plot([2, 3, 5, 10])
plt.show()

plt.plot([1, 2, 3 ,4], [2, 3, 5, 10], 'ro')
plt.show()
data_dict = {'x' : [1, 2, 3], 'y': [2, 3, 5]}
plt.plot('x', 'y', data = data_dict)
plt.show()




plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X-Label')
plt.ylabel('Y-label')
plt.show()

#라벨과 그래프 사이의 여백
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X-Axis', labelpad=15)
plt.ylabel('Y-Axis', labelpad=20)
plt.show()


plt.plot([1,2,3,4],[2,3,5,10])
plt.xlabel('X-Axis', labelpad=15, fontdict = {'family':'serif', 'color':'deeppink', 'weight': 'normal', 'size':'xx-large'})
plt.show()

dict1 = {1:2, 2:3, 3:4}
dict1.values()
