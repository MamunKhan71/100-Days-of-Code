import time


def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        after_time = time.time()
        time_diff = after_time - current_time
        print(f"Function Name : {function.__name__}\nRun Speed: {round(time_diff, 2)}s")

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
