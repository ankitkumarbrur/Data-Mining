import numpy as np
import pandas as pd

wine = pd.read_csv('wine.csv')
print("\nWine Dataset:")
print("\nMean:\t{}\nStandard Deviation:\t{}".format(wine.standa))

wine = wine.apply(lambda x: (x - x.mean()) / x.std() , axis = 0)
wine.describe()

iris = pd.read_csv('iris.csv')
iris = iris.iloc[:,0 : 4]
iris.describe()

iris = iris.apply(lambda x: (x - x.mean()) / x.std() , axis = 0)
iris.describe()