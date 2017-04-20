import numpy as np

#arr = np.zeros(shape=(1,10000))

#train_set = np.random.uniform(-1,1,10000)
#test_set = np.random.uniform(-1,1,10000)

#for i in range(0, 10):
    #arr[0][i] = ((s1[i], s2[i]), 2*s1[i] - s2[i] + np.random.normal(0, 0.01))

#epsilon = np.random.normal(0, variance, m)
#thetaJ = (0, 0)


# theta = (xt * x)^-1 * xty
def generate(interval, m, deviation):
	xtrain_1 = np.random.uniform(interval[0], interval[1], m)
	xtrain_2 = np.random.uniform(interval[0], interval[1], m)
	xtrain = []
	ytrain = np.zeros(m)

	for i in range(m):
		xtrain.append([xtrain_1[i], xtrain_2[i]])
	return xtrain, ytrain




def closed_form(m, k, x, y, deviation):
	print('x')

train_set, values = generate((-1, 1), 10000, 0.1)
print(len(train_set))
print(len(train_set[1]))
