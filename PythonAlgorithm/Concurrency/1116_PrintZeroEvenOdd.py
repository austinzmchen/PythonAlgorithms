from threading import Semaphore, Thread

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.num = 0
        self.sem_zero = Semaphore(1)
        self.sem_odd = Semaphore(0)
        self.sem_even = Semaphore(0)
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.sem_zero.acquire()
            printNumber(0)
            self.num += 1
            #
            if self.num % 2 == 0:
                self.sem_even.release()
            else:
                self.sem_odd.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.sem_even.acquire()
            printNumber(self.num)
            self.sem_zero.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.sem_odd.acquire()
            printNumber(self.num)
            self.sem_zero.release()

    def run(self):
      def printNumber(n):
        print(n, end="")
        
      d1 = Thread(name='daemon1', target=self.zero, args=(printNumber,))
      d2 = Thread(name='daemon2', target=self.even, args=(printNumber,))
      d3 = Thread(name='daemon3', target=self.odd, args=(printNumber,))

      d1.start()
      d2.start()
      d3.start()

      d1.join()
      d2.join()
      d3.join()


ins = ZeroEvenOdd(2)
ins.run()
print("")
