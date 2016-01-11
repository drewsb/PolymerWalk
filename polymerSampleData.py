import numpy as np
from pylab import *
from matplotlib import pyplot

data = [[6, 19.129], [8, 22.731], [10, 25.451666666666668], [12, 28.13175], [14, 30.6082], [16, 32.92], [18, 35.069], [20, 36.9155], [25, 38.09788888888889], [30, 40.5353], [35, 41.44527272727273], [40, 43.60641666666667], [50, 45.49946153846154], [60, 47.1095], [70, 48.71393333333334], [80, 50.0323125], [90, 51.258764705882356], [100, 52.34838888888889]]
datax=[]
datay=[]

for each in data:
    datax.append(each[0])
    datay.append(each[1])

scatter(datax,datay)  #Creates a histogram of the rolls
title("Scatter Plot of Average Number of Monomers", loc='center')  
plt.xlabel("Lattice Sites"); plt.ylabel("Monomers")  
show()