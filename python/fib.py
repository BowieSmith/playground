def fibslow(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibfast(n):
    if n < 0:
        return -1
    if n < len(fibfast.memoized):
        return fibfast.memoized[n]
    else:
        fibfast.memoized.append(fibfast(n - 1) + fibfast(n - 2))
        return fibfast.memoized[n]
fibfast.memoized = [0,1]

