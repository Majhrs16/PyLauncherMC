from threading import Thread

class _dThread(Thread):
    def __init__(self, funcion, *args, **kw):
        super().__init__()
        self.funcion = funcion
        self.args = args
        self.kwargs = kw

    def run(self):
        self.funcion(*self.args, **self.kwargs)

    def start(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Thread.start(self)

def dThread(func):
    def decorator(*args, **kw):
        return _dThread(func, *args, **kw)
    return decorator

if __name__ == "__main__":
    @dThread
    def Func(abc):
        print(abc)

    x = Func(123)
    x.start(daemon = False)
    x.start(daemon = True)
    x.start(daemon = True)
    print("OK")
    exit()
