def fibslow(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibslow(n - 1) + fibslow(n - 2)

def fibfast(n):
    if n < 0:
        return -1
    if n < len(fibfast.memoized):
        return fibfast.memoized[n]
    else:
        fibfast.memoized.append(fibfast(n - 1) + fibfast(n - 2))
        return fibfast.memoized[n]
fibfast.memoized = [0,1]

def fib_no_recur(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    print(a)
