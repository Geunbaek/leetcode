class MRUQueue:

    def __init__(self, n: int):
        self.q = [i for i in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        el = self.q[k - 1]
        self.q.remove(el)
        self.q.append(el)
        return el

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)