from functools import wraps

def logData(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        for arg in args:
            print(arg)
        print("in decorator wrapper")
        import pdb; pdb.set_trace()
        func(*args, **kwargs)
    return wrap

@logData
def addNum(a,b):
    return(a+b)

@logData
def subNum(a,b):
    return(a,b)

@logData
def multNum(a,b):
    return(a,b)




print(addNum(2,3))
