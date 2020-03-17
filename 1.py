import pandas as pd
import numpy as np
import matplotlib as mpl
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("Pokemon.csv")

x = dataFrame[0:5]['Name']
y = dataFrame[0:5]['Attack']

bars = plt.bar(x, y)
interger = 0
patters = ['&', '*', 'o', '^', '#']
for bar in bars:
    bar.set_hatch(patters[interger])
    interger = interger+1
    if interger > 2:
        interger = 0

plt.savefig('barchart.png', dpi=100)
plt.show()
