class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        alpha_set = set(source)

        for char in target:
            if char not in alpha_set:
                return -1
        
        n = len(source)
        index = 0
        count = 0

        for char in target:
            if index % n == 0:
                count += 1

            while source[index % n] != char:
                index += 1
                if index % n == 0:
                    count += 1

            index += 1
        return count
