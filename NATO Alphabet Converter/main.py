def my_decorator(f):
    def wrapped(*args, **kwargs):
        print('before function')
        response = f(*args, **kwargs)
        print('after function')
        return response
    print('decorating', f)
    return wrapped

@my_decorator
def my_function(a, b):
    print('in function')
    return a + b