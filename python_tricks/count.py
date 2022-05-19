
def dec_count(fn):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        fn()
        count =+ 1
        print(f'function {fn.__name__}() was called {count} time/-s')
        return count
    return wrapper


@dec_count
def func():
    print('Hello Johan!')

func()
func()