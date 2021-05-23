from time import time
def performance(function):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = function(*args, **kwargs)
        t2 = time() - t1
        print(f'it took {t2} ms')
        return result
    return wrapper
@performance
def long_time(limit=20000):
    result =[]
    for i in range(0,limit):
      result.append(i*20)
    return result
long_time(10000000)
    