import pandas as pd
import numpy as np

info = np.array(['P','A','N','D','A','S'])
a = pd.Series(info)
#print(a)

list=['Pandas','Numpy']
b = pd.DataFrame(list)
#print(b)

x = pd.Series(3,index=[0,1,2,3,4,5])
#print(x)

y = pd.Series(['H','E','L','L','O','O'],index=[0,1,2,3,4,5])
print(y)

print(y.index)
print(y.values)
print(y.ndim)
print(y.dtype)
print(y.size)