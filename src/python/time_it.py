from timeit import timeit
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timed_func = lambda: func(*args, **kwargs)
        exec_time = timeit(timed_func, number=1)
        print(f"Execution time of {func.__name__}: {exec_time:.6f} seconds")
        return timed_func()

    return wrapper


if __name__ == '__main__':
    @time_it
    def get_2d_ints():
        return [i for i in range(10,100)]
    
    @time_it
    def get_2d_ints_v2():
        return list(range(10,100))
    
    print(get_2d_ints())
    print(get_2d_ints_v2())