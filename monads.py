def f1(x): return x + 1

def f2(x): return x + 2

def f3(x): return x + 3

def unit(x):
    return (x, [x])  # init first arg

def bind(t, f):  # additional logic for chain calls
    res = f(t[0])
    return (res, t[1] + [res])

def pipeline(e, *functions):  # make chain. we can use bind(bind(bind(unit(x), f1), f2), f3) against
    for f in functions:
        e = bind(e, f)
    return e

 
init_ = 0
pipeline(unit(init_), f1, f2, f3)
