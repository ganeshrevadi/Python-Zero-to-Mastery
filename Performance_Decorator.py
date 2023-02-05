from time import time 
def performance(fn):
    def wrap(*args , **kwargs):
        t1 = time()
        result = fn(*args , **kwargs)
        t2 = time()
        print(f' It took {t2 - t1}s')
        return result
    return wrap

@performance
def long_time():
    for i in range(999999):
        i*7

long_time()    