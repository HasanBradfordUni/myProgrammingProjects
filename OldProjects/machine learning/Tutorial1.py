#importing the numpy library
import numpy as np
#importing the SciPy library
from scipy import stats

#creating a 1D array
a = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

#calculating the mean
mean = np.mean(a)

#calculating the median
median = np.median(a)

#calculating the mode
mode = stats.mode(a)

#printing the mean, median and mode
print("Mean: ", np.around(mean, 2))
print("Median: ", median)
print("Mode: ", mode[0])
print("Mode Count: ", mode[1])

