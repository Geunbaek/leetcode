class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy = []
        free = []

        meetings.sort()
        now_room_id = 0
        for s, e in meetings:
            while busy and busy[0][0] <= s:
                end, room_id, cnt = heapq.heappop(busy)
                heapq.heappush(free, (room_id, end, cnt))
                
            if free:
                room_id, end, cnt = heapq.heappop(free)
                heapq.heappush(busy, (e, room_id, cnt + 1))
            else:
                if now_room_id < n:
                    heapq.heappush(busy, (e, now_room_id, 1))
                    now_room_id += 1
                else:
                    duration = e - s
                    end, room_id, cnt = heapq.heappop(busy)
                    heapq.heappush(busy, (end + duration, room_id, cnt + 1))

        min_room_id = n
        max_count = 0
        while busy:
            end, room_id, cnt = heapq.heappop(busy)
            if cnt > max_count:
                max_count = cnt
                min_room_id = room_id
            elif cnt == max_count:
                min_room_id = min(min_room_id, room_id)

        while free:
            room_id, end, cnt = heapq.heappop(free)
            if cnt > max_count:
                max_count = cnt
                min_room_id = room_id
            elif cnt == max_count:
                min_room_id = min(min_room_id, room_id)
        return min_room_id 
        