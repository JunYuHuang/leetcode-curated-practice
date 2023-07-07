# My O(N) S class, O(1) T `set()` method, O(LogN) `get()` method binary search solution
class TimeMap:

    def __init__(self):
        # `store` stores subhashmaps that map each `key` to an array
        # of subarrays of size 2 where each subarray holds the int
        # timestamp at `sub[0]` and string value at `sub[1]`
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        l = 0
        r = len(values) - 1
        res = None
        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] < timestamp:
                res = values[m][1]
                l = m + 1
            else: # values[m][0] > timestamp
                r = m - 1
        return res if res else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
