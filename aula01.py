import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

data = load_iris()
iris = pd.DataFrame(data['data'], columns=data.feature_names)
target = data.target

# Importando o algoritmo de SVM

from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

svc = SVC(gamma='auto')

#Testando o modelo 'svc' na nossa base 'iris'
cv_result = cross_val_score(svc, iris, target, cv=10, scoring='accuracy')
#Retorna a acurácia em porcentagem do nosso modelo
print('Acurácia com cross validation:', cv_result.mean()*100)


plt.scatter(iris['sepal length (cm)'], iris['petal width (cm)'], c=target)
plt.title('Iris')