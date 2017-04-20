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
		ytrain[i] = 2*xtrain_1[i] - xtrain_2[i] + np.random.normal(0, 0.01)
	return np.asmatrix(xtrain), ytrain

def closed_form(X, y, k):
	if k > len(X):
		print('k too large')
	#print(X[:k])
	X = X[:k]
	y = y[:k]
	#print(len(X))
	xtrans_x = np.matmul(X.T, X)
	xtrans_xinv = xtrans_x.I
	xtrans_xinv_xtrans = np.matmul(xtrans_xinv, X.T)
	closed = np.matmul(xtrans_xinv_xtrans, y)
	return closed

# GRADIENT DESCENT


def gradientDescent(x, y, theta, alpha, m, numIterations):
    N = len(x)
    w = np.zeros((x.shape[1], 1))
    eta = alpha
    old = np.zeros(shape=(1000, 1))
    old = np.asmatrix(old)
    count = 0
    while True:
    	error = x*w - y
    	if (2-w[0]) < 0.001:
    		#print(2-w[0])
    		break
    	if eta > 0.001:
    		eta /= 2
    	gradient = x.T * error / N
    	w = w - eta * gradient
    	count += 1
    	#print(count)
    return w, count
#def gradient_descent():



