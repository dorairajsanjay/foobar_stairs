# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import matplotlib.pyplot as plt
import pandas as pd

# Scientific libraries
import numpy as np
from scipy.optimize import curve_fit

df = pd.read_csv("/Users/sdorai000/Downloads/exp_vals.csv")

x=df["x"]
y=df["y"]

def exponential_func(x, a, b, c):
    return a*np.exp(-b*x)+c

popt, pcov = curve_fit(exponential_func, x, y, p0=(1, 1e-6, 1))

a,b,c = popt
print(popt)
print(a,b,c)

y=map(lambda z: exponential_func(z,a,b,c),x)

df = pd.DataFrame(
    {'x': x,
     'y': y
    })

plt.plot(df.x,df.y)
plt.show()