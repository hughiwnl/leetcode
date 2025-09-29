class TimeMap:

    def __init__(self):
        self.keyStore = {} # empty dict

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore: # if its not there
            self.keyStore[key] = [] # intisialize in dict with value of empty list
        self.keyStore[key].append([value,timestamp]) # append to list with value and stamp [["bar", 1], ["bar2", 4]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key,[]) #gets the list of keystore, else returns empty array [["bar", 1], ["bar2", 4]]
        l = 0
        r = len(values) - 1
        while l<=r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)