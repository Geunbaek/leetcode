class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 != n2: return False

        diff_s1 = defaultdict(int)
        diff_s2 = defaultdict(int)
        diff_count = 0
        swap_count = 0

        for c1, c2 in zip(s1, s2):
            if c1 != c2:

                if (c1 in diff_s2 and c2 in diff_s1):
                    swap_count += 1
                    
                diff_count += 1
                diff_s1[c1] += 1
                diff_s2[c2] += 1

        if diff_count == 0:
            return True

        if diff_count == 2 and swap_count == 1:
            return True

        return False