use std::collections::VecDeque;

impl Solution {
    pub fn bfs(grid: &Vec<Vec<i32>>) -> i32 {
        if grid[0][0] != 0 {
            return -1
        }
        
        let mut q: VecDeque<(usize, usize, i32)> = VecDeque::new();
        q.push_back((0, 0, 1));
        
        let mut visited = [[0; 101]; 101];
        visited[0][0] = 1;
        
        let dx = [-1, -1, 0, 1, 1, 1, 0, -1];
        let dy = [0, -1, -1, -1, 0, 1, 1, 1];
        
        while let Some((x, y, count)) = q.pop_front() {
            if x == grid.len() - 1 && y == grid[0].len() - 1 {
                return count;
            }
            
            for i in 0..8 {
                let nx = (x as isize + dx[i]) as usize;
                let ny = (y as isize + dy[i]) as usize;
                
                if !(0 <= nx && nx < grid[0].len() && 0 <= ny && ny < grid.len()) {
                    continue;
                }
                
                if visited[ny][nx] == 1 {
                    continue;
                }
                
                if grid[ny][nx] != 0 {
                    continue;
                }
                
                visited[ny][nx] = 1;
                q.push_back((nx, ny, count + 1));
            }
        }
        return -1;
    }
    
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        return Solution::bfs(&grid)
    }
}