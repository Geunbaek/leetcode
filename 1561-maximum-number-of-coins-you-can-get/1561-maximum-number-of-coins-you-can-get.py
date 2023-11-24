class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = deque(piles)
        answer = 0
        while q:
            _min = q.popleft()
            first, second = q.pop(), q.pop()
            answer += second
        
        return answer
            
        