using PyPlot

f(x) = -sin(x[1]^2/2 - x[2]^2/4 + 3) * cos(2x[1] + 1 - exp(x[2]))

function fplot(f)
    x = range(-2.5, stop=2.5, length=200)
    y = range( -1.5, stop=1.5, length=100)
    u = [f([x,y]) for y in y, x in x]
    
    gcf().set_size_inches(12,5)
    contour(x, y, u, 25, colors="k", linewidths=0.5)
    contourf(x, y, u, 25)
    axis("equal")
    colorbar()
    return
end

fplot(f)
show() 

function df(x)
    a1 = x[1]^2/2 - x[2]^2/4 + 3
    a2 = 2x[1] + 1 - exp(x[2])
    b1 = cos(a1)*cos(a2)
    b2 = sin(a1)*sin(a2)
    return -[x[1]*b1 - 2b2, -x[2]/2*b1 + exp(x[2])*b2]
end

function gradient_descent(f, df, x0, α=0.1; tol=1e-4, maxiter=500)
    x = x0
    xs = [x0]
    for i = 1:maxiter
        gradient = df(x)
        if sqrt(sum(gradient.^2)) < tol
            break
        end
        x -= α*gradient
        push!(xs, x)
    end
    println("\nxs: ", xs)
    return xs
end

function plot_path(xs)
    plot(first.(xs), last.(xs), "w.", markersize=6)
    plot(first.(xs), last.(xs), "r", linewidth=1)
end

x0s = [[-2,.5], [0,.5], [2.2,-0.5]];

fplot(f)
title("Gradient descent, fixed \$\\alpha\$")
for x0 in x0s
    xs = gradient_descent(f, df, x0, 0.3)
    plot_path(xs)
    #println("Path length = $(length(xs)), ||gradient|| = $(sqrt(sum(df(xs[end]).^2)))")
end
show()