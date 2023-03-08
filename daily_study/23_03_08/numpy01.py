import numpy as np
np1 = np.random.randint(0,100,(10,10))
np.zeros((10,10))
np.ones((10,10))
np.shape(np1)
np.ndim(np1)


arr3 = np.zeros((10,10,10))
print(arr3)

#원하는 숫자로 배열생성
arr6 = np.full((10,10),10)
arr6
#원래 있던 모양과 같은 행렬 생성
np.zeros_like(arr6)
#np.ones_like(arr6)
#np.full_like(arr6,10)


#빈 행렬생성
arr7 = np.empty((10,10,10))

#사이즈 변경
#resize

#모양 재설정 reshape
arr10 = np.arange(0,10).reshape(5,2)
arr10

# 1차원으로 변경
# arr10.flatten()
