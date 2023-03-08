import sklearn.model_selection
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
for key, value in iris.items():
    print(f'{key} => {value}')
    
iris_df,label = load_iris(return_X_y=True,as_frame=True)
label

#학습용데이터와 테스트용 데이터를 나눔
#sklearn.model_selection.train_test_split
#stratify 비율대로 샘플링
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(iris_df, label)
len(X_train), len(X_test), len(y_train), len(y_test)

#테스트 비율 8:2
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(iris_df, label, test_size=0.2)
len(X_train), len(X_test), len(y_train), len(y_test)

#검증용 학습 중간중간에 수행
#마무리하고 테스트는 val로 배번


#학습모델 생성
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
#테스트용 데이터 예측
model.predict(X_test)
#예측 성공률 확인
model.score(X_test, y_test)


#성능평가 모듈 및 함수 sklearn.metrics.accuracy_score
from sklearn.metrics import accuracy_score
y_pred= model.predict(X_test)
#분류 성공 비율
accuracy_score(y_test, y_pred)
#개수
accuracy_score(y_test, y_pred, normalize=False)
import numpy as np
X_test
new_data = np.array([1.2, 0.3 ,2.3, 3.5]).reshape(1, 4)
new_data
new_pred = model.predict(new_data)

accuracy_score(new_pred, new_pred)
accuracy_score(new_pred, new_pred,normalize=False)
