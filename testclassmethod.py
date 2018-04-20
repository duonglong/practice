class foo():
    def __init__(self):
        pass

    @classmethod
    def bar(cls, n):
        print cls, n


x = foo()
x.bar(1)
