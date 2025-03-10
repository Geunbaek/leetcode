class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def is_vowel(c):
            return c in ["a", "e", "i", "o", "u"]

        n = len(word)
        left = 0
        right = 0
        vowel_cache = {}
        not_vowel_count = 0
        answer = 0

        next_consonant = [0] * len(
            word
        )  
        next_consonant_index = len(word)

        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if not is_vowel(word[i]):
                next_consonant_index = i

        while right < n:
            char = word[right]

            if is_vowel(char):
                vowel_cache[char] = vowel_cache.get(char, 0) + 1
            else:
                not_vowel_count += 1

            while not_vowel_count > k:
                left_char = word[left]

                if is_vowel(left_char):
                    vowel_cache[left_char] = vowel_cache.get(left_char) - 1
                    if vowel_cache[left_char] == 0:
                        del vowel_cache[left_char]
                else:
                    not_vowel_count -= 1

                left += 1

            while left < n and len(vowel_cache) == 5 and not_vowel_count == k:
                answer += next_consonant[right] - right

                left_char = word[left]

                if is_vowel(left_char):
                    vowel_cache[left_char] = vowel_cache.get(left_char) - 1
                    if vowel_cache[left_char] == 0:
                        del vowel_cache[left_char]
                else:
                    not_vowel_count -= 1

                left += 1

            right += 1
        return answer
