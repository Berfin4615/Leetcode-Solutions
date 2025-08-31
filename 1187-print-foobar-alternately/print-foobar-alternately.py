class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooDone = threading.Semaphore(1)
        self.barDone = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.fooDone.acquire()
            printFoo()
            self.barDone.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.barDone.acquire()
            printBar()
            self.fooDone.release()