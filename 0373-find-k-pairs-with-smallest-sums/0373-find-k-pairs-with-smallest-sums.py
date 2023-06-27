import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        
        h = []
        answer = []
        
        heapq.heappush(h, (nums1[0] + nums2[0], (0, 0)))
        
        visited = set()
        
        while len(answer) < k and h:
            s, (i, j) = heapq.heappop(h)
            answer.append((nums1[i], nums2[j]))
            
            if i + 1 < n and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(h, (nums1[i + 1] + nums2[j], (i + 1, j)))
                
            if j + 1 < m and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(h, (nums1[i] + nums2[j + 1], (i, j + 1)))

        return answer   