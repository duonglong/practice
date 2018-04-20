class foo(object):
    def __init__(self, fget):
        self.fget = fget
        fget()


@foo
def bar():
    print "123"
