from datetime import datetime

def timeit(function):
    def wrapper(*args, **kwargs):
       # print(function.__name__)
        start = datetime.now()
        res = function(*args, **kwargs)
        finish = datetime.now()
       # print(finish - start)
        return res

    return wrapper
