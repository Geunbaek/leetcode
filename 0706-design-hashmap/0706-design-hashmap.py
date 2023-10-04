class MyHashMap:

    def __init__(self):
        self.cache = dict()
        

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.cache[key]
        

    def remove(self, key: int) -> None:
        if key not in self.cache:
            return 
        del self.cache[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)