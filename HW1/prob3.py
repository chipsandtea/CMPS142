import numpy as np

arr = np.zeros(shape=(1,10000))

s1 = np.random.uniform(-1,1,10000)
s2 = np.random.uniform(-1,1,10000)

for i in range(0, 10):
    arr[0][i] = ((s1[i], s2[i]), 2*s1[i] - s2[i] + np.random.normal(0, 0.01))

for i in range(len(arr[1])):
    print(arr[0][i])