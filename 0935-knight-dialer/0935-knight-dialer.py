class Solution:
    def knightDialer(self, n: int) -> int:
        def recur(depth, cur):
            if depth >= n - 1:
                return 1
            
            if (depth, cur) in memo:
                return memo[(depth, cur)]
            
            x, y = board_map[cur]
            ret = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) not in board_pos_map:
                    continue
                ret += recur(depth + 1, board_pos_map[(nx, ny)]) % MOD
            memo[(depth, cur)] = ret % MOD
            return memo[(depth, cur)]
                
            
        r = 4
        c = 3
        MOD = 1_000_000_007
        memo = {}
        dx = [-1, 1, 2, 2, 1, -1, -2, -2]
        dy = [-2, -2, -1, 1, 2, 2, 1, -1]
        board_map = {
            1: (0, 0), 2: (1, 0), 3: (2, 0),
            4: (0, 1), 5: (1, 1), 6: (2, 1),
            7: (0, 2), 8: (1, 2), 9: (2, 2),
            0: (1, 3)
        }
        board_pos_map = {
            (0, 0): 1, (1, 0): 2, (2, 0): 3,
            (0, 1): 4, (1, 1): 5, (2, 1): 6,
            (0, 2): 7, (1, 2): 8, (2, 2): 9,
            (1, 3): 0
        }
        
        answer = 0
        
        for i in range(10):
            answer += recur(0, i)
            answer %= MOD
        return answer
    