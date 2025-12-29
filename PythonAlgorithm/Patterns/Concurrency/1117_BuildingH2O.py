from threading import Semaphore, Thread

# works in Java
class H2O:
    def __init__(self):
        self.sem_o = Semaphore(2)
        self.sem_h = Semaphore(0)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.sem_o.acquire()
        releaseHydrogen()
        self.sem_h.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # self.sem_h.acquire(2) # this value 2 is the boolean `blocking` parameter, not the semaphore value
        self.sem_h.acquire()
        self.sem_h.acquire() # this won't work either because 2 oxygen threads might each get 1 and cause deadlock
        releaseOxygen()
        self.sem_o.release(2)


from threading import Semaphore
from threading import Barrier

class H2O_2:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        # a Barrier -- if a thread reaches it, it can cross it, only if a predefined number of other threads have also arrived.
        self.bar_assembling = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.sem_h:
            self.bar_assembling.wait()
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.sem_o:
            self.bar_assembling.wait()
            releaseOxygen()