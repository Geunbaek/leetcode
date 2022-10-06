class TimeMap:

    def __init__(self):
        self.dict = dict()      
        self.timeDict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([timestamp, value])
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        maxTime = 0
        ret = ""
        
        left, right = 0, len(self.dict[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.dict[key][mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
                
        if right < 0 or right >= len(self.dict[key]):
            return ""
        return self.dict[key][right][1]
    
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)