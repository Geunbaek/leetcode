class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        h = []
        
        meetings.sort(key = lambda x: (x[0], -x[-1]))
                
        now_room_id = 0
        for s, e in meetings:
            if not h:
                heapq.heappush(h, (e, now_room_id, 1))
                now_room_id += 1
                continue

            end, room_id, cnt = heapq.heappop(h)
            if end <= s:
                min_room_id = room_id
                temp = [(end, room_id, cnt)]
                while h:
                    end, room_id, cnt = heapq.heappop(h)
                    if end <= s:
                        min_room_id = min(min_room_id, room_id)
                    temp.append((end, room_id, cnt))
                for end, room_id, cnt in temp:
                    if min_room_id == room_id:
                        heapq.heappush(h, (e, room_id, cnt + 1))
                    else:
                        heapq.heappush(h, (end, room_id, cnt))
            else:
                if now_room_id == n:
                    duration = e - s
                    heapq.heappush(h, (end + duration, room_id, cnt + 1))
                else:
                    heapq.heappush(h, (end, room_id, cnt))
                    heapq.heappush(h, (e, now_room_id, 1))
                    now_room_id += 1
        print(h)
        max_count = 0
        answer = n
        while h:
            e, r, c = heapq.heappop(h)
            if max_count < c:
                max_count = c
                answer = r
            elif max_count == c:
                answer = min(answer, r)
        
        return answer 