class RandomizedSet:

    def __init__(self):
        self.cache = set()
        self.values = []
        self.index_cache = dict()

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False

        self.cache.add(val)
        self.values.append(val)
        self.index_cache[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False

        removed_value_index = self.index_cache[val]
        self.index_cache[val] = len(self.values) - 1
        self.index_cache[self.values[-1]] = removed_value_index

        self.values[-1], self.values[removed_value_index] = self.values[removed_value_index], self.values[-1]

        self.cache.remove(val)
        self.values.pop()
        return True

    def getRandom(self) -> int:
        random_index = random.randrange(0, len(self.values))
        return self.values[random_index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()