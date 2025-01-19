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

def gradient_descent(f, df, x0, alpha=0.1, tol=1e-4, maxiter=3):
    x = x0
    xs = [x0]
    for i in range(maxiter):
        gradient = df(x)
        if (np.sqrt(np.sum(gradient**2)) < tol):
            break
        x -= alpha * gradient
        print("PYTHON x: ", x)
        xs.append(x.copy()) ## This x.copy() is EXTREMELY important!!!
    print("PYTHON xs: ", xs)
    return xs

x0s = [[-2, 0.5], [0, 0.5], [2.2, -0.5]]


for x0 in x0s:
    xs = gradient_descent(f, df, x0, 0.3)

# Evaluate Python function at test points
python_results = xs[0:3]
#print("Python Results:", python_results)