import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from statistics import mean
from matplotlib import style

colnames = ['year','adjective','keyword','text']

data = pd.read_csv("final.csv", names=colnames)

texts = data.text.tolist()
years = data.year.tolist()
years = [str(x) for x in years]

print('number of segments')
print(len(texts))

decade_counts = [0]*16

# COHA data (to normalize by word count for each decade)

colnamesCOHA = ['DECADE','FICTION','POPULAR','NEWSPAPERS','NON-FICTION','TOTAL','% FICTION']

dataCOHA = pd.read_csv("coha_content.csv", names=colnamesCOHA)

COHA_TOTAL = dataCOHA.TOTAL.tolist()
COHA_TOTAL = COHA_TOTAL[5:21]
COHA_TOTAL = [x.replace(',',"") for x in COHA_TOTAL]
COHA_TOTAL = [float(x) for x in COHA_TOTAL]
COHA_TOTAL = [x/1000000.0 for x in COHA_TOTAL]


for year in years:
	ind = years.index(year)
		
	if year.startswith('185'):
		decade_counts[0] += 1
		
	if year.startswith('186'):
		decade_counts[1] += 1
	
	if year.startswith('187'):
		decade_counts[2] += 1 
		
	if year.startswith('188'):
		decade_counts[3] += 1 
		
	if year.startswith('189'):
		decade_counts[4] += 1 
		
	if year.startswith('190'):
		decade_counts[5] += 1 
		
	if year.startswith('191'):
		decade_counts[6] += 1 
		
	if year.startswith('192'):
		decade_counts[7] += 1 
		
	if year.startswith('193'):
		decade_counts[8] += 1 
		
	if year.startswith('194'):
		decade_counts[9] += 1 
		
	if year.startswith('195'):
		decade_counts[10] += 1 
		
	if year.startswith('196'):
		decade_counts[11] += 1 
		
	if year.startswith('197'):
		decade_counts[12] += 1 	
	
	if year.startswith('198'):
		decade_counts[13] += 1 
		
	if year.startswith('199'):
		decade_counts[14] += 1 
		
	if year.startswith('200'):
		decade_counts[15] += 1 
			
			
decades = [1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]

# get counts / millions of words for decade

normalized_count = [x/y for x, y in zip(decade_counts, COHA_TOTAL)]

# plot
	
import matplotlib.pyplot as plt

# a = decades
# b = decade_counts

# plt.scatter(a,b)
# plt.ylabel("Adjective-Entity Pairs")
# plt.xlabel("Decades")
# c = np.polyfit(a, b, 1)
# d = np.poly1d(c)
# plt.plot(a,d(a),"r")

# plt.show()

# normalized

x = decades
y = normalized_count
plt.scatter(x,y,color='b')
plt.ylabel("Positive Sentiment Adjective-Entity Pairs (Per Million Words)")


xs = np.array(x, dtype=np.float64)
ys = np.array(y, dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    
    b = mean(ys) - m*mean(xs)
    
    return m, b

m, b = best_fit_slope_and_intercept(xs,ys)

print("frequency data (sentiment):")
print(pearsonr(x, y))
print(m,b)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r")

plt.show()

