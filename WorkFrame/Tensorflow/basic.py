import tensorflow as tf
tensor =tf.constant([3,4,5])
print(tensor)
#탠서가 필요한 이유?

x1 x2 x3 input
w1 w2 w3 weight
?? x1w1 x2w2 x3w3

#복잡스러..
#행렬을 사용해서 곱해서 한거번에 계산하기 좋음
tensor1  = tf.constant([3,4,5])
tensor2  = tf.constant([6,7,8])
print(tensor1 +tensor2)
tensor3 = tf.constant([[1,2],[3,4]])
#tf.add()
print(tf.add(tensor1, tensor2))
#행렬의 곱
tf.matmul()
tensor4 = tf.zeros(10)
#2행2열 0들어있는 행렬생성
tensor5 = tf.zeros([2,2])

tensor6= tf.zeros([2,2,3])
tensor6

#모냥은?
tensor6.shape


tensor7 = tf.constant([[1,2,3],[4,5,6]])
tensor7.shape
print(tensor)
tensor_float = tf.constant([1.2,3.2,3.2])
print(tensor_float)
#tf.constant([]) 변하지 않는 상수(고정)
#tf.variable => weight 저장하는 곳(변동)
w = tf.Variable(1.0)
print(w)
#변경이 쉬우므로 tf.Variable사용
#사용법 w.numpy()
print(w.numpy())
#수정할당
w.assign(2)
#레이가 이미 있는 걸로 사용함.

import tensorflow as tf
height= [170,180,175,160]
shoes = [260,270,265,255]
# (y=신발) = a(x=키) + b
# 키에 따른 신발사이즈의 회귀선을 그리고 싶당
# 데이터를 하나만 있다고 가정
height = 170
shoes = 260
shoes = height * a + b
#가중치 정의
a= tf.Variable(0.1)
b= tf.Variable(0.2)
# def loss_function():
#     return tf.square(실제값- 예측값)
def loss_function():
    foresee = height * a + b
    return tf.square(260- foresee)

#알아서 업데이트 해줌 Adam이 성능 굳
opt = tf.keras.optimizers.Adam(learning_rate = 0.1)
#opt.minimize(손실함수, var_list = [a,b]) list는 경사하강법으로 업데이트할 목록
opt.minimize(loss_function, var_list = [a,b])
#뿅 경사하강 한번
# 최적값이 나올 때까지 반복
#300번 반복
for i in range(300):
    opt.minimize(loss_function, var_list = [a,b])
    print(a.numpy(),b.numpy())
    
180*1.519+1.619
