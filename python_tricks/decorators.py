
def uppercase(fn):
    print('start dec')
    def wrapper(*args):
        print('wrap start')
        original_result = fn(*args)
        modified_result = original_result.upper()
        print('end wrap')
        return modified_result
    print('end dec')
    return wrapper


def null_decorator(fn):
    print('We are in the decorator')
    return fn

def greet(value):
    print(f'{value} function!')
    return 'Hello!'
new_greet = uppercase(greet)
new_greet('my')

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'ТРАССИРОВКА: вызвана {func.__name__}() '
              f'c {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'ТРАССИРОВКА: {func.__name__}() '
              f'вернула {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

say('Jane', 'Hello world!')
