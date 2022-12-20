class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(now_room):
            for room in rooms[now_room]:
                if visited[room] == 0:
                    visited[room] = 1
                    dfs(room)
        visited = [0 for _ in range(len(rooms))] 
        visited[0] = 1
        
        dfs(0)
        
        return 0 not in visited
        
        