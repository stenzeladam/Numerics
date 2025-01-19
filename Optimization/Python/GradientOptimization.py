import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -np.sin(x[0]**2 / 2 - x[1]**2 / 4 + 3) * np.cos(2 * x[0] + 1 - np.exp(x[1]))

def fplot(f):
    
    x = np.linspace(-2.5, 2.5, 200)
    y = np.linspace(-1.5, 1.5, 100)
    
    X, Y = np.meshgrid(x, y)
    U = np.array([[f([X[i, j], Y[i, j]]) for j in range(X.shape[1])] for i in range(X.shape[0])])
    plt.figure(figsize=(12, 5))
    plt.contour(X, Y, U, 25, colors='k', linewidths=0.5)
    contour = plt.contourf(X, Y, U, 25, cmap='viridis')
    plt.axis('equal')
    plt.colorbar(contour)
    plt.show()

# function for the gradient
def df(x):
    a1 = x[0]**2 / 2 - x[1]**2 / 4 + 3
    a2 = 2 * x[0] + 1 - np.exp(x[1])
    b1 = np.cos(a1) * np.cos(a2)
    b2 = np.sin(a1) * np.sin(a2)
    return -np.array([x[0] * b1 - 2 * b2, -x[1] / 2 * b1 + np.exp(x[1]) * b2])

def gradient_descent(f, df, x0, alpha=0.1, tol=1e-4, maxiter=500):
    x = x0
    xs = [x0]
    for i in range(maxiter):
        gradient = df(x)
        if (np.sqrt(np.sum(gradient**2)) < tol):
            break
        x -= alpha * gradient
        xs.append(x)
    print("\nxs: ", xs, "\n")
    return xs

def plot_path(xs):
    x_coords = [x[0] for x in xs]  # equivalent to first.(xs) in Julia
    y_coords = [x[1] for x in xs]  # equivalent to last.(xs) in Julia
    
    plt.plot(x_coords, y_coords, 'w.', markersize=6)
    plt.plot(x_coords, y_coords, 'r-', linewidth=1)


x0s = [[-2, 0.5], [0, 0.5], [2.2, -0.5]]

# Plot the function's contour
x = np.linspace(-2.5, 2.5, 200)
y = np.linspace(-1.5, 1.5, 100)
X, Y = np.meshgrid(x, y)
Z = np.array([[f([X[i, j], Y[i, j]]) for j in range(X.shape[1])] for i in range(X.shape[0])])

plt.figure(figsize=(12, 5))
plt.contour(X, Y, Z, 25, colors='k', linewidths=0.5)
plt.contourf(X, Y, Z, 25)
plt.axis('equal')
plt.colorbar()
plt.title("Gradient descent, fixed $\\alpha$")

# Apply gradient descent and plot the paths
for x0 in x0s:
    xs = gradient_descent(f, df, x0, 0.3)
    plot_path(xs)
    path_length = len(xs)
    gradient_norm = np.linalg.norm(df(xs[-1]))
    #print(f"Path length = {path_length}, ||gradient|| = {gradient_norm}")

plt.show()