class TimeMap:

    def __init__(self):
        self.key_dict: [str, int] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_dict.setdefault(key, {})
        self.key_dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if time2value := self.key_dict.get(key, {}):
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
        return res


timeMap = TimeMap();
timeMap.set("foo", "bar", 1);  # store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         # return "bar"
timeMap.get("foo", 3);         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); # store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         # return "bar2"
timeMap.get("foo", 5);         # return "bar2"