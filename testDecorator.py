def foo(barz):
    def real_foo(func):
        def wrapper():
            print barz
            func()
        return wrapper
    return real_foo

@foo('555')
def bar():
    print '456'

bar()