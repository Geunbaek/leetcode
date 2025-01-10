class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:        
        answer = []
        alpha = defaultdict(int)

        for word2 in words2:
            counter = Counter(word2)

            for key in counter.keys():
                alpha[key] = max(alpha[key], counter[key])


        for word in words1:
            counter1 = Counter(word)

            for key in alpha.keys():
                if counter1[key] < alpha[key]:
                    break
            else:
                answer.append(word)
       
        return answer

