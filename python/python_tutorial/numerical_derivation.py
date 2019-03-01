def derivative(f):
    dx = 0.00001
    def deriv(x):
        return (f(x + dx) - f(x)) / dx
    return deriv
