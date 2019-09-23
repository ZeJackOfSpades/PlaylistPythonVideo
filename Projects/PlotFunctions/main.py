#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return x**4 - 4*x**2 + 3*x

X = np.linspace(-3, 3, 50, endpoint=False)
F = p(X)
plt.plot(X,F)
plt.show()