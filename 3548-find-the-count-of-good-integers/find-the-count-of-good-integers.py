import math
import itertools

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Precompute factorials up to n (n <= 10).
        fact = [math.factorial(i) for i in range(n+1)]
        
        def count_multiset_permutations(freq, n):
            """Count distinct permutations for given frequency distribution (list of 10 numbers)
            while subtracting the ones with a leading zero.
            """
            total = fact[n]
            for c in freq:
                total //= fact[c]
            if freq[0] > 0:
                lead0 = fact[n-1]
                lead0 //= fact[freq[0]-1]
                for d in range(1, 10):
                    lead0 //= fact[freq[d]]
            else:
                lead0 = 0
            return total - lead0

        def generate_distributions(total, bins=10):
            """Generate all tuples of length 'bins' of non-negative integers that sum up to total."""
            if bins == 1:
                yield (total,)
            else:
                for i in range(total + 1):
                    for tail in generate_distributions(total - i, bins - 1):
                        yield (i,) + tail
        
        def unique_permutations(lst):
            """Return all unique permutations of the list lst."""
            return set(itertools.permutations(lst))
        
        def exists_valid_palindrome(half_list, mid, is_even, n, k):
            """
            Check if there's at least one valid ordering of the half (and a middle digit if applicable)
            that forms a palindrome without a leading zero and divisible by k.
            """
            # Special case for n == 1
            if len(half_list) == 0:
                return (mid % k == 0)
            
            for perm in unique_permutations(half_list):
                if perm[0] == 0:  # Skip orderings that would produce a leading zero.
                    continue
                if is_even:
                    num_str = "".join(map(str, perm)) + "".join(map(str, perm[::-1]))
                else:
                    num_str = "".join(map(str, perm)) + str(mid) + "".join(map(str, perm[::-1]))
                if int(num_str) % k == 0:
                    return True
            return False

        total_good = 0
        
        if n % 2 == 0:
            # Even-length number: let L = n/2.
            L = n // 2
            for H in generate_distributions(L, bins=10):
                # Ensure that at least one nonzero digit appears in the half.
                if L > 0 and sum(H[d] for d in range(1, 10)) == 0:
                    continue
                half_list = []
                for d in range(10):
                    half_list.extend([d] * H[d])
                # Build the full frequency distribution (each digit count is doubled)
                f = [2 * cnt for cnt in H]
                if exists_valid_palindrome(half_list, mid=None, is_even=True, n=n, k=k):
                    total_good += count_multiset_permutations(f, n)
        else:
            # Odd-length numbers: n = 2L + 1.
            L = (n - 1) // 2
            if L == 0:
                # Single digit case (n == 1): digit must be nonzero.
                for d in range(1, 10):
                    if d % k == 0:
                        total_good += 1
            else:
                for H in generate_distributions(L, bins=10):
                    # For a valid half, at least one nonzero digit is required.
                    if sum(H[d] for d in range(1, 10)) == 0:
                        continue
                    half_list = []
                    for d in range(10):
                        half_list.extend([d] * H[d])
                    for mid in range(10):
                        # Build frequency distribution: double the half's counts and add one for the middle digit.
                        f = [2 * H[d] for d in range(10)]
                        f[mid] += 1
                        if exists_valid_palindrome(half_list, mid, is_even=False, n=n, k=k):
                            total_good += count_multiset_permutations(f, n)
        return total_good
