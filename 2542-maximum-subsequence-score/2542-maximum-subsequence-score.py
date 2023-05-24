import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        z = list(zip(nums1, nums2))
        z.sort(key = lambda x: -x[-1])
        _sum = 0
        _min = float('inf')
        
        h = []
        
        for i in range(k):
            n1, n2 = z[i]
            _sum += n1
            heapq.heappush(h, (n1, n2))
            
        answer = _sum * z[k - 1][1]
        for i in range(k, len(z)):
            n1, n2 = z[i]
            sn1, sn2 = heapq.heappop(h)
            _sum -= sn1
            _sum += n1
            heapq.heappush(h, (n1, n2))
            answer = max(answer, _sum * n2)
        
        return answer
            
            
        
            
        