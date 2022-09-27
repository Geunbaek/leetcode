class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def check(index):
            left, right = index, index
            
            while left > 0 and dominoes[left] == '.':
                left -= 1
            
            while right < len(dominoes) - 1 and dominoes[right] == '.':
                right += 1
                
            return left, right
            
        dominoes = list(dominoes)
        newDominoes = ["." for _ in range(len(dominoes))]
        
        for i in range(len(dominoes)):
            if dominoes[i] == '.':
                left, right = check(i)
                if dominoes[left] != '.' and dominoes[right] != '.':
                    if dominoes[left] == 'R' and dominoes[right] == 'R':
                        newDominoes[i] = dominoes[left]
                    elif dominoes[left] == 'L' and dominoes[right] == 'L':
                        newDominoes[i] = dominoes[right]
                    elif dominoes[left] == 'R' and dominoes[right] == 'L':
                        if i - left > right - i:
                            if dominoes[right] == 'R': continue
                            newDominoes[i] = dominoes[right]
                        elif i - left < right - i:
                            if dominoes[left] == 'L': continue
                            newDominoes[i] = dominoes[left]
                   
                elif dominoes[left] == '.':
                    if dominoes[right] == 'R': continue
                    newDominoes[i] = dominoes[right]
                elif dominoes[right] == '.':
                    if dominoes[left] == 'L': continue
                    newDominoes[i] = dominoes[left] 
            else:
                newDominoes[i] = dominoes[i]
    
        return "".join(newDominoes)
                
            