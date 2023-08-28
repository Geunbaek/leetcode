from collections import deque

class MyStack:

    def __init__(self):
        self.queues = [deque(), deque()]
        self.main = 0
        

    def push(self, x: int) -> None:
        self.queues[self.main].append(x)
        

    def pop(self) -> int:
        main = self.main
        sub = 1 if self.main == 0 else 0
        
        while len(self.queues[main]) > 1:
            self.queues[sub].append(self.queues[main].popleft())
        
        self.main = sub
        return self.queues[main].popleft()
        

    def top(self) -> int:
        main = self.main
        sub = 1 if self.main == 0 else 0
        
        while len(self.queues[main]) > 1:
            self.queues[sub].append(self.queues[main].popleft())
        
        last = self.queues[main].popleft()
        self.main = sub
        self.queues[sub].append(last)
        return last
        

    def empty(self) -> bool:
        return len(self.queues[self.main]) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()