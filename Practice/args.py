def add(*args):
    result = 0
    for n in args:
        result += n

    return result

print(add(10,20,30,40))
