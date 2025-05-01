class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def check(mid):
            available_worker = deque()

            worker_index = 0
            p = pills
            print()
            for task_index in range(mid - 1, -1, -1):
                while worker_index < mid and workers[worker_index] + strength >= tasks[task_index]:
                    available_worker.append(workers[worker_index])
                    worker_index += 1
                if not available_worker:
                    return False

                _max = available_worker[0]

                if _max >= tasks[task_index]:
                    available_worker.popleft()
                else:
                    if p == 0:
                        return False
                    p -= 1
                    available_worker.pop()
            return True

        
        n, m = len(tasks), len(workers)
        
        tasks = sorted(tasks)
        workers = sorted(workers, reverse=True)

        left, right = 1, min(n, m)
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer



        
        
                
