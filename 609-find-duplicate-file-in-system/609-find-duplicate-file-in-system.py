from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(list)
        
        for path in paths:
            path = path.split()
            directoryPath = path[0]
            fileInfos = path[1:]
    
            for fileInfo in fileInfos:
                fileInfo = fileInfo.split("(")
                fileName = fileInfo[0]
                fileContent = fileInfo[1][:-1]
                files[fileContent].append(directoryPath + "/" + fileName)
                
        return list(filter(lambda x: len(x) >= 2, [val for key, val in files.items()]))
        
            
        