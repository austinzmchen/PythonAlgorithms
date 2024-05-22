from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def find_employee_free_time(schedule):
    result = []
    all_slots = [slot for person_sch in schedule for slot in person_sch]
    all_slots.sort(key=lambda x: x.start)

    curr_slot = all_slots[0]
    for i in range(1, len(all_slots)):
      if curr_slot.end >= all_slots[i].start:
        curr_slot = Interval(curr_slot.start, all_slots[i].end)
      else:
        result.append(Interval(curr_slot.end, all_slots[i].start))
        curr_slot = all_slots[i]

    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
