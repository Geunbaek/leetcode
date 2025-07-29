class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        def num_to_bin(num):
            return bin(num)[2:]

        def bin_to_num(b_num):
            return int(b_num, 2)
        
        def arr_to_num(arr):
            return bin_to_num("".join(list(map(lambda x: "1" if x else "0", arr))))

        def add_num_to_arr(arr, num):
            b_num = num_to_bin(num)
            last = 29
            ret = copy.deepcopy(arr)

            for i in range(len(b_num)):
                if b_num[len(b_num) - i - 1] == "0":
                    continue
                ret[last - i] += 1
            return ret

        def sub_num_to_arr(arr, num):
            b_num = num_to_bin(num)
            last = 29
            ret = copy.deepcopy(arr)
            for i in range(len(b_num)):
                if b_num[len(b_num) - i - 1] == "0":
                    continue
                ret[last - i] -= 1

            return ret

        def sub_bin_arr(arr1, arr2):
            ret = []

            for a1, a2 in zip(arr1, arr2):
                ret.append(a1 - a2)

            return ret

        n = len(nums)
        prefix = [[0 for _ in range(30)]]

        for num in nums:
            prefix.append(add_num_to_arr(prefix[-1], num))

        answer = []

        r = 0
        for l in range(n):
            _max = arr_to_num(sub_bin_arr(prefix[-1], prefix[l]))
            while r < n and arr_to_num(sub_bin_arr(prefix[r], prefix[l])) != _max:
                r += 1
            answer.append(r - l if r - l > 0 else 1)
        return answer