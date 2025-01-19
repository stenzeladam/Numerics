using PyPlot

f(x) = -sin(x[1]^2/2 - x[2]^2/4 + 3) * cos(2x[1] + 1 - exp(x[2]))

function df(x)
    a1 = x[1]^2/2 - x[2]^2/4 + 3
    a2 = 2x[1] + 1 - exp(x[2])
    b1 = cos(a1)*cos(a2)
    b2 = sin(a1)*sin(a2)
    return -[x[1]*b1 - 2b2, -x[2]/2*b1 + exp(x[2])*b2]
end

function gradient_descent(f, df, x0, alpha=0.1; tol=1e-4, maxiter=3)
    x = x0
    xs = [x0]

    for i = 1:maxiter
        gradient = df(x)
        if sqrt(sum(gradient.^2)) < tol
            break
        end
        x -= alpha*gradient
        println("JULIA x: ", x)
        push!(xs, x)
    end
    println("JULIA xs: ", xs)
    return xs
end

x0s = [[-2, 0.5], [0, 0.5], [2.2, -0.5]]

global xs = []
for x0 in x0s
    global xs = gradient_descent(f, df, x0, 0.3)
end

# Evaluate Julia function at test points
#julia_results = [df(point) for point in test_points]
#println("Julia Results: ", xs[1:3])
