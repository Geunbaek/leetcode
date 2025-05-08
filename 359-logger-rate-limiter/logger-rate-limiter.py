class Logger:

    def __init__(self):
        self.cache = defaultdict(int)
        self.duration = 10
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.cache:
            prev = self.cache[message]
            if prev + self.duration > timestamp:
                return False

        self.cache[message] = timestamp
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)