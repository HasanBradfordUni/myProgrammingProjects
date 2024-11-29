#Program to find what is the correlation coefficient between two sets of data
"""Formula to be used: n(Σxy)−(Σx)(Σy)/√[nΣx^2−(Σx)^2][nΣy^2−(Σy)^2]
where n is the number of data points, 
Σxy is the sum of the product of the data points, 
Σx is the sum of the first data set, Σy is the sum of the second data set, 
Σx^2 is the sum of the squares of the first data set, and Σy^2 is the sum of the squares of the second data set."""

import math

def mean(data):
    return sum(data)/len(data)

def correlationCoefficient(data1, data2):
    n = len(data1)
    sum_x = sum(data1)
    sum_y = sum(data2)
    sum_xy = sum([data1[i]*data2[i] for i in range(n)])
    sum_x2 = sum([data1[i]**2 for i in range(n)])
    sum_y2 = sum([data2[i]**2 for i in range(n)])
    return (n*sum_xy - sum_x*sum_y)/math.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))

videoLengths = [11, 8, 18, 5, 10, 9]
views = [28, 111, 55, 64, 35, 45]
print("Correlation Coefficient: ")
print(correlationCoefficient(videoLengths, views))
