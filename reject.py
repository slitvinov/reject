import random
import matplotlib.pylab as plt
import math
import numpy as np


def g(x):
	return math.sin(x)


def gsample():
	# x = Finver(y), where F = int(sin(x)/2, x, 0, x)
	y = random.uniform(0, 1)
	return math.pi - math.acos(2 * y - 1)


def f(x):
	return math.fabs(math.sin(x * x / 2)) * x * (math.pi - x) / 2


random.seed(123)
M = 2
S = []
Ay = []
Rx = []
Ry = []
T = 200
for i in range(T):
	while True:
		x = gsample()
		u = random.uniform(0, 1)
		y = M * g(x) * u
		if y <= f(x):
			Ay.append(y)
			break
		else:
			Rx.append(x)
			Ry.append(y)
	S.append(x)

X = np.linspace(0, math.pi, 100)
pp = [f(x) for x in X]
plt.figure()
plt.hist(S, bins=20, density=True, fill=False, color='k')
plt.plot(X, pp, '-k', label="f(x)")
plt.legend()
plt.savefig("hist.svg")

gq = [M * g(x) for x in X]
plt.figure()
plt.plot(X, gq, '--k', label="g(x)")
plt.plot(X, pp, '-k', label="f(x)")
plt.plot(Rx, Ry, 'xk', label="rejected")
plt.plot(S, Ay, 'ok', fillstyle='none', label="accepted")
plt.legend()
plt.savefig("reject.svg")
