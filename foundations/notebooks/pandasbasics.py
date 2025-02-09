import pandas as pd
import numpy as np

#series is a one-dimensional labeled array that can hold any data type (integers, floats, strings, objects, etc)

data = [35.467,63.951,80.94,60.655,127.061,64.511,318.523]
popl = pd.Series(data)

popl.name='G7 POPULATION (in millions)'

#custom index
popl.index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'UK', 'USA']
print(popl)

#accessing elements
print("\npopulation of France",popl['France'],"\n")  

#numeric positions can be accessed with iloc attribute
print(popl.iloc[1])

#selecting multiple elements; result is another series
print(popl[['France','Germany']])

#slicing works; but here upper limit is included
print(popl['Canada':'Italy'])

#boolean arrays-conditional selection
print(popl[popl>80])

print("mean of the population: ",popl.mean())
print("std of the population: ",popl.std())
print(popl[popl>popl.mean()])

print(popl*1000000)
print(np.log(popl))

print(popl[(popl>popl.mean())|~(popl<popl.std())])

#modifying series
popl.iloc[-1]=500
popl['Canada']=45
print(popl)
