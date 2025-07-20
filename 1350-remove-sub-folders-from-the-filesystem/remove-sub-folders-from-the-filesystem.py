class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TreeNode(None)

    def search(self, arr):
        node = self.root

        for c in arr:
            if node.is_end:
                return True

            if c in node.children:
                node = node.children[c]
            else:
                return False

        return False
            
    def push(self, arr):
        node = self.root

        for c in arr:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TreeNode(c)
                node = node.children[c]

        node.is_end = True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()  
        answer = []
        for file_path in folder:
            file_path_arr = file_path.split('/')
            if trie.search(file_path_arr):
                continue
            
            trie.push(file_path_arr)
            answer.append(file_path)

        return answer

