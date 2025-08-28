import threading

class Foo:
    def __init__(self):
        self.second_ready = threading.Event()
        self.third_ready = threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_ready.set() 


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_ready.wait() 
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_ready.set() 



    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_ready.wait() 
        # printThird() outputs "third". Do not change or remove this line.
        printThird()