class TimeMap:

    def __init__(self):
        self.key_dict: [str, int] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_dict.setdefault(key, {})
        self.key_dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_dict:
            return ""
        if (time2value := self.key_dict.get(key, {})) and timestamp in time2value:
            return time2value[timestamp]
        
        times = sorted(time2value.keys())
        l, r = 0, len(times) - 1
        res = ""
        
        while l <= r:
            mid = (l + r) // 2
            mid_time = times[mid]
            
            if mid_time == timestamp:
                return time2value[mid_time]

            if mid_time < timestamp:
                res = time2value[mid_time]
                l = mid + 1
            else:
                r = mid - 1

        return time2value[times[r]] if r >= 0 else ""
        # return res


timeMap1 = TimeMap();
timeMap1.set("foo", "bar", 1)    # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap1.get("foo", 1))    # return "bar"
print(timeMap1.get("foo", 3))    # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap1.set("foo", "bar2", 4)   # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap1.get("foo", 4))    # return "bar2"
print(timeMap1.get("foo", 5))    # return "bar2"


timeMap = TimeMap()
timeMap.set("love", "high", 10)
timeMap.set("love", "low", 20)
print(timeMap.get("love", 5))       # ""
print(timeMap.get("love", 10))      # high

print(timeMap.get("love", 15))      # high
print(timeMap.get("love", 20))      # low
print(timeMap.get("love", 25))      # low