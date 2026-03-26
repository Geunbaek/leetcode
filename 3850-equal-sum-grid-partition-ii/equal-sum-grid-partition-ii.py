from collections import defaultdict
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check_split(g: List[List[int]]) -> bool:
            r = len(g)
            c = len(g[0])
            
            top = defaultdict(int)
            bottom = defaultdict(int)
            
            # [최적화 1] 파이썬 내장 sum()을 활용하여 연산 횟수 감소
            bottom_total = 0
            for row in g:
                for val in row:
                    bottom[val] += 1
                bottom_total += sum(row) # 원소별로 더하는 대신 C-레벨로 구현된 sum() 사용

            top_total = 0

            # [최적화 2] 반복문 내부의 지역 변수 캐싱 및 불필요한 연산 제거
            for y in range(r - 1):
                row = g[y] # g[y]를 매번 찾지 않고 지역 변수에 캐싱
                top_len = y + 1
                bottom_len = r - top_len
                row_sum = 0
                
                for val in row:
                    bottom[val] -= 1
                    top[val] += 1
                    row_sum += val
                
                # 행 단위로 한 번에 더하고 빼기
                bottom_total -= row_sum
                top_total += row_sum

                if bottom_total == top_total:
                    return True
                
                # [최적화 3] abs() 함수 호출 제거: if 분기를 통해 크기 비교 후 단순 뺄셈
                if top_total > bottom_total:
                    diff = top_total - bottom_total
                    
                    if top_len == 1:
                        if diff == row[0] or diff == row[-1]: return True
                    elif c == 1:
                        if diff == g[0][0] or diff == row[0]: return True
                    elif top.get(diff, 0): # > 0 비교 생략 (파이썬에서 양수 정수는 True로 평가됨)
                        return True
                        
                else: # bottom_total > top_total 인 경우
                    diff = bottom_total - top_total
                    
                    if bottom_len == 1:
                        if diff == g[-1][0] or diff == g[-1][-1]: return True
                    elif c == 1:
                        if diff == g[y + 1][0] or diff == g[-1][0]: return True
                    elif bottom.get(diff, 0):
                        return True
                        
            return False

        if check_split(grid):
            return True
            
        return check_split([list(col) for col in zip(*grid)])