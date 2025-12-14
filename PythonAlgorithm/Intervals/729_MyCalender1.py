class MyCalendar729:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for b in self.bookings:
            if max(b[0], start) < min(b[1], end):
                return False
        #
        self.bookings.append([start, end])
        return True
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)