class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        
        node.is_end = True
        
    def contains(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
        
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recur(depth):
            if depth >= len(s):
                dp[-1] = 1
                return
            
            word = ""
            for i in range(depth, len(s)):
                word += s[i]
                if trie.contains(word) and dp[i] == 0:
                    dp[i] = 1
                    recur(i + 1)
    
        dp = [0 for _ in range(len(s))]
        trie = Trie()
        
        for word in wordDict:
            trie.insert(word)
            
        recur(0)
        return dp[-1]
        
        
        