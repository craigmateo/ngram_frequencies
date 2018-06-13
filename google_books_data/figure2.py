import nltk
import collections
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from statistics import mean
from matplotlib import style

colnames = ['year','AVG','NORMALIZED']
data = pd.read_csv("NA_Google_data_normalized1900.csv", names=colnames)

Years = data.year.tolist()
Avg_Freq = data.NORMALIZED.tolist()

Years.pop(0)
Avg_Freq.pop(0)

colnames_pop = ["YEAR","PERCENT_RURAL","NORMALIZED"]
data_pop = pd.read_csv("rural_pop_US_corr1900.csv", names=colnames_pop)

Years_pop = data_pop.YEAR.tolist()
Rural_pop = data_pop.NORMALIZED.tolist()

Years_pop.pop(0)
Rural_pop.pop(0)

x = [int(x) for x in Years]
y = [float(y) for y in Avg_Freq]

x_pop = [int(x) for x in Years_pop]
y_pop = [float(y) for y in Rural_pop]

plt.ylabel('Normalized value')
plt.xlabel('Year')

plt.plot(x, y, 'b*')
plt.plot(x_pop, y_pop, 'rs')

plt.legend(['Frequency', 'Rural Population'], loc='upper right')

xs = np.array(x, dtype=np.float64)
ys = np.array(y, dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    
    b = mean(ys) - m*mean(xs)
    
    return m, b

m, b = best_fit_slope_and_intercept(xs,ys)

print("frequency data:")
print(pearsonr(x, y))
print(m,b)

regression_line = [(m*x)+b for x in xs]
plt.scatter(xs,ys,color='#003F72')
plt.plot(xs, regression_line)

s = pd.Series(y_pop)
pop_inter = s.interpolate()

x_inter = np.array(x_pop, dtype=np.float64)
y_inter = np.array(pop_inter, dtype=np.float64)

def best_fit_slope_and_intercept(xinter,yinter):
    m = (((mean(xinter)*mean(yinter)) - mean(xinter*yinter)) /
         ((mean(xinter)*mean(xinter)) - mean(xinter*xinter)))
    
    b = mean(yinter) - m*mean(xinter)
    
    return m, b

m, b = best_fit_slope_and_intercept(x_inter,y_inter)
print("pop data:")
print(pearsonr(x_pop, y_inter))
print(m,b)

regression_line = [(m*x)+b for x in x_inter]

plt.scatter(xs,ys,color='#003F72')
plt.plot(xs, regression_line)

plt.show()


