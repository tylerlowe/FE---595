import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn import cross_validation
from sklearn.feature_selection import RFE

boston = load_boston()
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
bos['PRICE'] = boston.target
print(bos.head())

X = bos.drop('PRICE', axis = 1)
Y = bos['PRICE']

X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y, test_size = 0.33, random_state = 5)

lr = LinearRegression()
rfe = RFE(lr, 3)
rfe = rfe.fit(X_train, Y_train)
print(rfe.support_)
print(rfe.ranking_)
