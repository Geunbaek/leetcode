class Solution:
    def numberOfWays(self, corridor: str) -> int:
        s_count = corridor.count("S")

        if s_count < 2:
            return 0
        
        if s_count % 2 != 0:
            return 0
        
        if s_count == 2:
            return 1
        
        
        plants_area = [0]
        n = len(corridor)
        MOD = 1_000_000_007
        now_seat_count = 0
        
        for i in range(n):
            if corridor[i] == "S":
                now_seat_count += 1
                if now_seat_count > 2:
                    now_seat_count %= 2
                    plants_area.append(0)
            else:
                if now_seat_count == 2:
                    if not plants_area:
                        plants_area.append(0)
                    plants_area[-1] += 1
            
        
        answer = 1
     
        for area in plants_area[:-1]:
            answer *= (area + 1) 
            answer %= MOD
        return answer