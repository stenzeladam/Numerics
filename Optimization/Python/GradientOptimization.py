import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -np.sin(x[0]**2 / 2 - x[1]**2 / 4 + 3) * np.cos(2 * x[0] + 1 - np.exp(x[1]))

# Function for gradient
def df(x):
    a1 = x[0]**2 / 2 - x[1]**2 / 4 + 3
    a2 = 2 * x[0] + 1 - np.exp(x[1])
    b1 = np.cos(a1) * np.cos(a2)
    b2 = np.sin(a1) * np.sin(a2)
    return -np.array([x[0] * b1 - 2 * b2, -x[1] / 2 * b1 + np.exp(x[1]) * b2])

# Gradient Descent function with fixed alpha
def gradient_descent(f, df, x0, alpha=0.1, tol=1e-4, maxiter=500):
    x = x0
    xs = [x0]
    for i in range(maxiter):
        gradient = df(x)
        if np.sqrt(np.sum(gradient**2)) < tol:
            break
        x -= alpha * gradient
        xs.append(x.copy())
    return xs

# Gradient Descent function with line search
def line_search(f, direction, x, alpha_min=1/2**20, alpha_max=2**20):
    alpha = alpha_min
    fold = f(x)
    while True:
        if alpha >= alpha_max:
            return alpha
        fnew = f(x - alpha*direction)
        if fnew >= fold:
            return alpha/2
        else:
            fold = fnew
        alpha *= 2

def gradient_descent_line_search(f, df, x0, tol=1e-4, maxiter=500):
    x = x0
    xs = [x0]
    for i in range(maxiter):
        gradient = df(x)
        if np.sqrt(np.sum(gradient**2)) < tol:
            break
        alpha = line_search(f, gradient, x)
        x -= alpha * gradient
        xs.append(x.copy())
    return xs

def finite_difference_gradient(f, x, epsilon=1e-5):
    n = len(x)
    df = np.zeros(n)
    for k in range(n):
        x1 = np.copy(x)
        x1[k] += epsilon
        fP = f(x1)
        x1[k] -= 2*epsilon
        fM = f(x1)
        df[k] = (fP - fM) / (2*epsilon)
    return df

def finite_difference_hessian(f, x, epsilon=1e-5):
    n = len(x)
    ddf = np.zeros((n,n))
    f0 = f(x)
    for i in range(n):
        x1 = np.copy(x)
        x1[i] += epsilon
        fP = f(x1)
        x1[i] -= 2*epsilon
        fM = f(x1)
        ddf[i,i] = (fP - 2*f0 + fM) / (epsilon**2)
    for i in range(n):
        for j in range(i+1, n):
            x1 = np.copy(x)
            x1[i] += epsilon
            x1[j] += epsilon
            fPP = f(x1)
            x1[i] -= 2*epsilon
            fMP = f(x1)
            x1[j] -= 2*epsilon
            fMM = f(x1)
            x1[i] += 2*epsilon
            fPM = f(x1)
            ddf[i,j] = (fPP - fMP - fPM + fMM) / (4*epsilon**2)
            ddf[j,i] = ddf[i,j]
    return ddf


# Function to plot the path
def plot_path(xs):
    x_coords = [x[0] for x in xs]
    y_coords = [x[1] for x in xs]
    plt.plot(x_coords, y_coords, 'w.', markersize=6)
    plt.plot(x_coords, y_coords, 'r-', linewidth=1)

# Function to plot the function contour
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

x0s = [[-2, 0.5], [0, 0.5], [2.2, -0.5]]

# Gradient descent
fplot(f)
plt.title("Gradient descent, fixed $\\alpha$")
print("Gradient descent, fixed α")
for x0 in x0s:
    xs = gradient_descent(f, df, x0, 0.3)
    plot_path(xs)
    path_length = len(xs)
    gradient_norm = np.linalg.norm(df(xs[-1]))
    print(f"Path length = {path_length}, ||gradient|| = {gradient_norm}")
print("\n")
plt.show()

# Plotting with line search
fplot(f)
plt.title("Gradient descent, line searches for $\\alpha$")
print("Gradient descent, line searches for α")
for x0 in x0s:
    xs = gradient_descent_line_search(f, df, x0)
    plot_path(xs)
    path_length = len(xs)
    gradient_norm = np.linalg.norm(df(xs[-1]))
    print(f"Path length = {path_length}, ||gradient|| = {gradient_norm}")
print("\n")
plt.show()

# Plotting with using finite differences instead of the gradient function
fplot(f)
plt.title("Gradient descent, line searches for $\\alpha$, numerical gradients")
print("Gradient descent, line searches for α, numerical gradients")

for x0 in x0s:
    def num_df(x):
        return finite_difference_gradient(f, x)
    xs = gradient_descent_line_search(f, num_df, x0)
    plot_path(xs)
    path_length = len(xs)
    gradient_norm = np.linalg.norm(df(xs[-1]))
    print(f"Path length = {path_length}, ||gradient|| = {gradient_norm}")
print("\n")
plt.show()

# Plotting Newton's method
fplot(f)
plt.title("Newton's method, line searches for $\\alpha$, numerical gradients and Hessians")
print("Newton's method, line searches for α, numerical gradients and Hessians")
x0s = [[-2,0.0], [0,.5], [2.,0.]]
for x0 in x0s:
    def search_dir(x):
        hessian = finite_difference_hessian(f, x)
        gradient = finite_difference_gradient(f, x)
        return np.linalg.solve(hessian, gradient)
    xs = gradient_descent_line_search(f, search_dir, x0)
    plot_path(xs)
    path_length = len(xs)
    gradient_norm = np.linalg.norm(df(xs[-1]))
    print(f"Path length = {path_length}, ||gradient|| = {gradient_norm}")
print("\n")
plt.show()
