
class MYclass:
    loc = 'jeju'    
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f'나의 고향은{MYclass.loc}입니다.')#클래스 변수의 경우 이렇게 표현하는게 바람직
#클래스
a = MYclass('hl')
a.display()



from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pandas as pd

#parameters에 들어가는 커널은 선형과 비선형 등을 적용할 수도 있다.
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.2, random_state =121)
parameters = {'max_depth': [1,2,3],'min_samples_split':[2,3]}

dtree = DecisionTreeClassifier()
grid_dtree = GridSearchCV(dtree, param_grid=parameters, cv = 3, refit =True)
grid_dtree.fit(X_train, y_train)

scores_df = pd.DataFrame(grid_dtree.cv_results_)
scores_df[['params','rank_test_score','mean_test_score','std_test_score']]

print(f'GridSearchCV 최적 파라미터: {grid_dtree.best_params_}')
print(f'GridSearchCV 최고 정확도: {grid_dtree.best_score_}')