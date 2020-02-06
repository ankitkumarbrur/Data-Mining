import numpy as np
import pandas as pd

wine = pd.read_csv('wine.csv')
print('-'*100,"\nWine Dataset:")
print(wine.describe())
print("\nMean:\n{}\n\nStandard Deviation:\n{}".format(wine.mean(),wine.mean()))

wine = wine.apply(lambda x: (x - x.mean()) / x.std() , axis = 0)
print('-'*100,"\n\nStandardized Wine Dataset:")
print(wine.describe())
print("\nMean:\n{}\n\nStandard Deviation:\n{}".format(wine.mean(),wine.mean()))

 
iris = pd.read_csv('iris.csv')
iris = iris.iloc[:,0 : 4]
print('-'*100,"\nIris Dataset:")
print(iris.describe())
print("\nMean:\n{}\n\n\nStandard Deviation:\n{}".format(iris.mean(),iris.mean()))


iris = iris.apply(lambda x: (x - x.mean()) / x.std() , axis = 0)
print('-'*100,"\n\nStandardized Iris Dataset:")
print(iris.describe())
print("\nMean:\n{}\n\n\nStandard Deviation:\n{}".format(iris.mean(),iris.mean()))
 