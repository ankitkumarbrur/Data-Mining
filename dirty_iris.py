import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dirty_iris_rules as dir
pd.set_option('display.max_rows',157)

dataset = pd.read_csv("dirty_iris.csv")
dataset = dataset.replace([np.inf, -np.inf], np.nan)
dataset[dataset.iloc[:,:4]<0] = np.nan

n = len(dataset)
n1 = len(dataset.dropna())

print('\nNumber of total observations:          {}\nNumber of complete observations:        {}'.format(n,n1))
print('\nPercentage of complete observations:    {}%'.format(int((n1/n)*100)))


# print(dir.check_species(dataset))
# print(dir.check_validity(dataset))
# print(dir.check_petal_length_width(dataset))
# print(dir.check_sepal_length(dataset))
# print(dir.check_sepal_petal(dataset))

breaks_rule = (dir.check_species(dataset) & dir.check_petal_length_width(dataset) & dir.check_sepal_length(dataset) & dir.check_sepal_petal(dataset) )

print(breaks_rule)

# a = dir.check_species(dataset)
# print(a[0:10])