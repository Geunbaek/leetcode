class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        answer = []

        ball_cache = {}
        color_cache = {}

        for ball, color in queries:
            if color in color_cache:
                color_cache[color] += 1
            else:
                color_cache[color] = 1
            
            if ball in ball_cache:
                prev_color = ball_cache[ball]
                color_cache[prev_color] -= 1

                if color_cache[prev_color] == 0:
                    del color_cache[prev_color]
                    
            ball_cache[ball] = color
            answer.append(len(color_cache))
        return answer                

