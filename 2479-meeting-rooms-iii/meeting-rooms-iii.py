class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        cache = [0 for _ in range(n)]
        meetings.sort()
        used_h = []
        unused_h = []

        for i in range(n):
            heappush(unused_h, (i))

        for start, end in meetings:
            while used_h and used_h[0][0] <= start:
                end_time, room_no = heappop(used_h)
                heappush(unused_h, room_no)

            if unused_h:
                room_no = heappop(unused_h)
                cache[room_no] += 1
                heappush(used_h, (end, room_no))
            else:
                end_time, room_no = heappop(used_h)
                cache[room_no] += 1
                heappush(used_h, (end + (end_time - start), room_no))

        return cache.index(max(cache))
        
        