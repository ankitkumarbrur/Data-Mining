import pandas as pd  
import numpy as np  
a = pd.Series(['Java', 'C', 'C++'])  
a=a.map({'Java': 'Core','C':'core1','C++':'core2'})
print(a.map('I like {}'.format))
print(a.map('I like {}'.format, na_action='ignore'))