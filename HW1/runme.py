from prob3 import generate, closed_form, gradientDescent
import numpy as np

print('=======CLOSED  FORM=======')
print('=====OUTPUT ~ [2, -1]=====')
train_set, values = generate((-1, 1), 10000, 0.1)
test_set, vals = generate((-1, 1), 10000, 0.1)
k = [10, 100, 1000, 10000]
print(values.shape)
print('TRAIN SET')
for i in k:
	k_val = i
	val = closed_form(train_set, values, i)
	print('kval: \t' + str(k_val) + '\t val:' + str(val))
	print('t1 error: ' + str(2-val[0,0]) + ' t2 error:' + str(-1-val[0,1]))
print('TEST SET')
for i in k:
	k_val = i
	val = closed_form(test_set, vals, i)
	print('kval: \t' + str(k_val) + '\t val:' + str(val))
	print('t1 error: ' + str(2-val[0,0]) + ' t2 error:' + str(-1-val[0,1]))
#print(closed_form(train_set, values, 500))
print('=====GRADIENT DESCENT=====')
X, y = generate((-1, 1), 10000, 0.01)

#theta_closed = closed_form(X, y, 1000)
theta = np.array([0, 0])

#print(X.shape)
y = np.asmatrix(y)
y = y.T
#print(y.shape)
#print(theta.shape)

val = closed_form(X, y, 10000)
print('kval: \t' + str(k_val) + '\t val:' + str(val))
w, ctr= gradientDescent(X, y, theta, 1, 0.01, 20)
print(1)
print(w)
print(ctr)
print('ERROR')
print(w-val)
w, ctr= gradientDescent(X, y, theta, 0.1, 0.01, 20)
print(0.1)
print(w)
print(ctr)
print('ERROR')
print(w-val)
w, ctr= gradientDescent(X, y, theta, 0.01, 0.01, 20)
print(0.01)
print(w)
print(ctr)
print('ERROR')
print(w-val)
w, ctr= gradientDescent(X, y, theta, 0.001, 0.01, 20)
print(0.001)
print(w)
print(ctr)
print('ERROR')
print(w-val)


'''
J_closed = mean_squared_error(X, y, theta_closed)
theta_1, T1 = batch_gradient_descent(X, y, 1)
theta_2, T2 = batch_gradient_descent(X, y, 0.1)
theta_3, T3 = batch_gradient_descent(X, y, 0.01)
theta_4, T4 = batch_gradient_descent(X, y, 0.001)

print('1: ' + (str(mean_squared_error(X, y, theta_1) - J_closed)) + ' ' + str(T1))
print('2: ' + (str(mean_squared_error(X, y, theta_2) - J_closed)) + ' ' + str(T2))
print('3: ' + (str(mean_squared_error(X, y, theta_3) - J_closed)) + ' ' + str(T3))
print('4: ' + (str(mean_squared_error(X, y, theta_4) - J_closed)) + ' ' + str(T4))'''