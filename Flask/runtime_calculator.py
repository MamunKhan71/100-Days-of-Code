import time

current_time = time.time()


def speed_calc_decorator(function):
    def wrapper_function():
        function()
        total_time = time.time() - current_time
        print(total_time)

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
