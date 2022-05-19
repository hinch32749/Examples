v = 1000


def func(a, b, c):
    """Docstring"""
    # li = []
    # li.append(a)
    # li.append(b)
    # li.append(c)
    x = 10
    y = 20
    z = x + y
    return a + b + c


print(func)
f = func
print(func.__closure__)

a = 255
b = a.__index__()
print(type(b))



class Inner(object):
    def __init__(self, value):
        self.value = value

    # def __iter__(self):
    #     print("hi")
    #     return self
    #
    # def __next__(self):
    #     return self.value

    def __contains__(self, item):
        print("Вызывается метод __contains__", item)
        return 'a'


a = Inner('hello')

# print("a" in a)


