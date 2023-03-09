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


#의사결정트리 학습모델 생성
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


#SVM 분류모형

#테스트 비율 8:2
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(iris['data'], iris['target'], test_size=0.2, random_state=12)
len(X_train), len(X_test), len(y_train), len(y_test)

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

#KNN prediction 최근접이웃
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy_score(y_test, y_pred)

new_data = np.array([1.2, 0.3, 2.3, 3.5]).reshape(1, 4)
new_pred = knn.predict(new_data)

accuracy_score(new_data, new_pred)



#교차 검증 CV

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import numpy as np
iris = load_iris()
features = iris['data']
label = iris['target']
dt_clf = DecisionTreeClassifier()
#다섯개의 fold로 나눔
kflod_data = KFold(n_splits=5)
n_iter = 0
#KFOLD 활용
for train_index, test_index in kflod_data.split(features):
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    dt_clf.fit(X_train, y_train)
    pred = dt_clf.predict(X_test)
    n_iter += 1
    #    
    accuracy = np.round(accuracy_score(y_test, pred), 4)

#이건 너무 귀찮음

#cross_val_score()
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.datasets import load_iris
iris = load_iris()
dt_clf = DecisionTreeClassifier()

data = iris['data']
label = iris['target']

scores = cross_val_score(dt_clf, data, label, cv=5)
print(f'각 교차검증별 정확도:{np.round(scores,2)}')
print(f'평균 검증 정확도{scores.mean():.4f}')

#여러 검증데이터를 확인할 경우
scores = cross_validate(dt_clf, data, label,scoring=['r2'], cv=5)
scores
print(round(scores['r2']))