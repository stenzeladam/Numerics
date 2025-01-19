import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -np.sin(x[0]**2 / 2 - x[1]**2 / 4 + 3) * np.cos(2 * x[0] + 1 - np.exp(x[1]))

def df(x):
    a1 = x[0]**2 / 2 - x[1]**2 / 4 + 3
    a2 = 2 * x[0] + 1 - np.exp(x[1])
    b1 = np.cos(a1) * np.cos(a2)
    b2 = np.sin(a1) * np.sin(a2)
    return -np.array([x[0] * b1 - 2 * b2, -x[1] / 2 * b1 + np.exp(x[1]) * b2])

def gradient_descent(f, df, x0, alpha=0.1, tol=1e-4, maxiter=500):
    x = x0
    xs = [x0]
    print(xs)
    for i in range(maxiter):
        gradient = df(x)
        if (np.sqrt(np.sum(gradient**2)) < tol):
            break
        x -= alpha * gradient
        xs.append(x)
    return xs

x0s = [[-2, 0.5], [0, 0.5], [2.2, -0.5]]


for x0 in x0s:
    xs = gradient_descent(f, df, x0, 0.3)

# Evaluate Python function at test points
python_results = xs[0:3]
#print("Python Results:", python_results)