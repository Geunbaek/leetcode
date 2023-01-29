import heapq

class LFUCache:
    
    def __init__(self, capacity: int):
        self.cache = dict()
        self.freqs = dict()
        self.capacity = capacity
    
    def update_freq(self, key):
        self.freqs[key] = self.freqs[key] + 1
        if self.freqs[key] not in self.cache:
            self.cache[self.freqs[key]] = OrderedDict()
                
 
        self.cache[self.freqs[key]][key] = self.cache[self.freqs[key] - 1][key]
            
        del self.cache[self.freqs[key] - 1][key]
        if len(self.cache[self.freqs[key] - 1]) == 0:
            del self.cache[self.freqs[key] - 1]
        
    def remove_LFU(self):
        freq_counter = 1
        k = None
        
        while k is None:
            if freq_counter in self.cache:
                k, v = self.cache[freq_counter].popitem(last=False)
                if len(self.cache[freq_counter]) == 0:
                    del self.cache[freq_counter]
            else:
                freq_counter += 1
        
        del self.freqs[k]
        
    def get(self, key: int) -> int:
        if key in self.freqs:
            self.update_freq(key)
                
            return self.cache[self.freqs[key]][key]
        else:
            return -1
          
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.freqs:
            self.update_freq(key)
            self.cache[self.freqs[key]][key] = value
        else:
            if len(self.freqs) == self.capacity:
                self.remove_LFU()
            
            if 1 not in self.cache:
                self.cache[1] = OrderedDict()
            self.freqs[key] = 1
            self.cache[1][key] = value
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)