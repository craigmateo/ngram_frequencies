import nltk
import collections
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

colnames = ['year','AVG']
data = pd.read_csv("NA_Google_data_normalized.csv", names=colnames)

Years = data.year.tolist()
Avg_Freq = data.AVG.tolist()

Years.pop(0)
Avg_Freq.pop(0)


colnamesCOHA = ['decade','AVG']
dataCOHA = pd.read_csv("COHA_normalized.csv", names=colnamesCOHA)

YearsCOHA = dataCOHA.decade.tolist()
Avg_FreqCOHA = dataCOHA.AVG.tolist()

YearsCOHA.pop(0)
Avg_FreqCOHA.pop(0)

x_coha = [float(x) for x in YearsCOHA]
y_coha = [float(y) for y in Avg_FreqCOHA]

colnames_pop = ["YEAR","PERCENT_RURAL","NORMALIZED"]
data_pop = pd.read_csv("rural_pop_US_corr.csv", names=colnames_pop)

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
plt.plot(x_coha, y_coha, 'go')
plt.plot(x_pop, y_pop,'rs')

plt.legend(['Frequency (Google Books)', 'Frequency (COHA)','Rural Population'], loc='upper left')

plt.show()







