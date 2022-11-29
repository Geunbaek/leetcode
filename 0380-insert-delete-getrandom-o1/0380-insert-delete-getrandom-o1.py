class RandomizedSet:

    def __init__(self):
        self.set = set();
        

    def insert(self, val: int) -> bool:
        is_contain = val in self.set
        if not is_contain:
            self.set.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        is_contain = val in self.set
        if is_contain:
            self.set.remove(val)
        return is_contain
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.set) - 1)
        return list(self.set)[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()