import random
import matplotlib.pylab as plt
import math
import numpy as np


def qstar(x):
	return math.sin(x)


def qsample():
	# x = Finver(y), where F = int(sin(x)/2, x, 0, x)
	y = random.uniform(0, 1)
	return math.pi - math.acos(2 * y - 1)


def pstar(x):
	return math.fabs(math.sin(x * x / 2)) * x * (math.pi - x) / 2


random.seed(123)
gamma = 2
S = []
Ay = []
Rx = []
Ry = []
T = 200
for i in range(T):
	while True:
		x = qsample()
		u = random.uniform(0, 1)
		y = gamma * qstar(x) * u
		if y <= pstar(x):
			Ay.append(y)
			break
		else:
			Rx.append(x)
			Ry.append(y)
	S.append(x)

X = np.linspace(0, math.pi, 100)
pp = [pstar(x) for x in X]
plt.figure()
plt.hist(S, bins=20, density=True, fill=False, color='k')
plt.plot(X, pp, '-k')
plt.savefig("hist.svg")

gq = [gamma * qstar(x) for x in X]
plt.figure()
plt.plot(X, pp, '-k')
plt.plot(X, gq, '--k')
plt.plot(Rx, Ry, 'xk')
plt.plot(S, Ay, 'ok', fillstyle='none')
plt.savefig("reject.svg")
