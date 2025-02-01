class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        cache = defaultdict(int)
        temp = deque(nums[:k])
        answer = []

        for num in temp:
            cache[num] += 1
        answer.append(len(cache))

        for num in nums[k:]:
            first = temp.popleft()
            cache[first] -= 1
            if cache[first] == 0:
                del cache[first]
                
            temp.append(num)
            cache[num] += 1
            answer.append(len(cache))

        return answer
            


        