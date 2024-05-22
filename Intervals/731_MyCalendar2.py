class MyCalendarTwo729:

    def __init__(self):
        self.double_booked = []
        self.single_booked = []

    def book(self, start: int, end: int) -> bool:
        for db in self.double_booked:
            if max(db[0], start) < min(db[1], end):
                return False
        #
        for db in self.single_booked:
            if max(db[0], start) < min(db[1], end):
                self.double_booked.append([max(db[0], start), min(db[1], end)])
        #
        self.single_booked.append([start, end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)