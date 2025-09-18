

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.cache = {}

        for userId, taskId, priority in tasks:
            heappush(self.pq, (-priority, -taskId, userId))
            self.cache[taskId] = {"priority": priority, "userId": userId}

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.pq, (-priority, -taskId, userId))
        self.cache[taskId] = {"priority": priority, "userId": userId}

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.cache[taskId]["userId"]
        heappush(self.pq, (-newPriority, -taskId, userId))
        self.cache[taskId]["priority"] = newPriority

    def rmv(self, taskId: int) -> None:
        del self.cache[taskId]
        

    def execTop(self) -> int:
        while self.pq:
            priority, taskId, userId = heappop(self.pq)
            if -taskId not in self.cache:
                continue
            if self.cache[-taskId]["priority"] != -priority:
                continue
            if self.cache[-taskId]["userId"] != userId:
                continue
            self.rmv(-taskId)
            return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()