import pandas as pd
data = pd.read_csv('gpascore.csv')
data = data.dropna()
print(data.isnull().sum())
# data = data.fillna(data.mean())
data.isnull().sum()
y = data.admit.values
x = []
for i,rows in data.iterrows():
    x.append([rows['gre'],rows['gpa'],rows['rank']])
print(x)

import tensorflow as tf
import numpy as np
model= tf.keras.models.Sequential([
    tf.keras.layers.Dense(64,activation = 'tanh'),#layer생성
    tf.keras.layers.Dense(128, activation = 'tanh'),#(노드의 개수) 보통 2의 제곱 수를 넣음
    tf.keras.layers.Dense(1,activation = 'sigmoid')
#마지막 결과물을 신경써서 나타내줌
#확률한개 예측할때는 1개
#확률은 0~1사이 값=> sigmoid 사용

])
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
#결과가 0과 1사이의 분류/확률예측일 경우
#loss 함수는 binary_crossentropy사용
# model.fit(x데이터[학습데이터], y데이터[결과데이터],epochs=10 학습횟수)
model.fit(np.array(x),np.array(y),epochs = 1500)
# x데이터 학습데이터를 리스트로 묶음.=> 그걸 리스트로 묶음
# y데이터 결과데이터 리스트 묶음


#예측
#x값만 넣으면 됨
predict= model.predict([[750, 3.7, 3],[400,2.2,1]])
print(predict)
#데이터 전처리 시 성능향상
#모델 튜닝 시 성능향
