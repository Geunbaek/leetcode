class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        arr = []
        answer = [0 for _ in range(len(obstacles))]
        
        for i, obstacle in enumerate(obstacles):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= obstacle:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == len(arr):
                arr.append(obstacle)
            else:
                arr[left] = obstacle
            answer[i] = left + 1
     
        return answer
                
"""

class Solution {
    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        int n = obstacles.length;
        int length = 0;
        int[] result = new int[n];
        int[] increasingSubseq = new int[n];
        for (int i = 0; i < n; ++i) {
            int left = 0, right = length;
            while (left < right) {
                int mid = (left + right) / 2;
                if (increasingSubseq[mid] <= obstacles[i])
                    left = mid + 1;
                else
                    right = mid;
            }
            result[i] = left + 1;
            if (length == left)
                length++;
            increasingSubseq[left] = obstacles[i];
        }
        return result;
    }
}
"""
        
        
        
        
        