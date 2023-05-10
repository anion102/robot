from time import time


def timing(func):
    def wrapper_func(*args, **kwargs):
        start = time()   # the unit is second
        print(start)
        result = func(*args, **kwargs)
        end = time()
        print(end)
        print("Elapsed time is : {}".format(start-end))
        return result
    return wrapper_func


def logging(func):
    def wrapper_func(*args, **kwargs):
        print("the request is: {}; {}".format(*args,**kwargs))
        result = func(*args, **kwargs)
        print("the response is : {}".format(result))
        return result
    return wrapper_func
