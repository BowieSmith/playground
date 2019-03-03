def cons(a,b):
    return lambda f : f(a,b)

def first(pair):
    return pair(lambda a, b : a)

def rest(pair):
    return pair(lambda a, b : b)

def to_string(l):
    def helper(l, string):
        if l is None:
            return f'{string[:-2]})'
        else:
            return helper(rest(l), f'{string}{first(l)}, ')
    return helper(l, '(')

def range(start, stop):
    if start > stop:
        return None
    else:
        return cons(start, range(start + 1, stop))

def map(proc, l):
    if l is None:
        return None
    else:
        return cons(proc(first(l)), map(proc, rest(l)))

def reduce(op, init, l):
    if l is None:
        return init
    else:
        return op(first(l), reduce(op, init, rest(l)))

def filter(pred, l):
    if l is None:
        return None
    if pred(first(l)):
        return cons(first(l), filter(pred, rest(l)))
    else:
        return filter(pred, rest(l))
