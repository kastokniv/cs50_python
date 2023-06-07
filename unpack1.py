def f(*args, **kwargs):
    ## if name given in f() use args or use kwargs
    print("Positional:", kwargs)


f(galleons=100, sickles=50, knuts=25)
