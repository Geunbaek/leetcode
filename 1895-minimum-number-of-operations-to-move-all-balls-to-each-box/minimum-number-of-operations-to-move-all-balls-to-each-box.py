class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0 for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j: continue
                if boxes[j] != "1": continue 
                answer[i] += abs(i - j)
        return answer