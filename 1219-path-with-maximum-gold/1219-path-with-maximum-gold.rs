use std::collections::{VecDeque, HashSet};

impl Solution {
    pub fn get_maximum_gold(grid: Vec<Vec<i32>>) -> i32 {
        fn dfs(grid: &Vec<Vec<i32>>, visited: &mut Vec<Vec<usize>>, x: usize, y: usize, total: i32, answer: &mut i32) {
            let r = grid.len();
            let c = grid[0].len();
            
            let dx = [-1, 0, 1, 0];
            let dy = [0, -1, 0, 1];
            let mut flag = false;
            
            for i in 0..4 {
                let nx = (x as i32 + dx[i]) as usize;
                let ny = (y as i32 + dy[i]) as usize;
                
                if !(nx < c && ny < r) {
                    continue;
                }
                
                if grid[ny][nx] == 0 {
                    continue;
                }
                
                if visited[ny][nx] == 1 {
                    continue;
                }
                
                visited[ny][nx] = 1;
                flag = true;
                dfs(grid, visited, nx, ny, total + grid[ny][nx], answer);
                visited[ny][nx] = 0;
            }
            if !flag {
                *answer = std::cmp::max(*answer, total);
            }
            
        }
        
        let r = grid.len();
        let c = grid[0].len();
        let mut visited = vec![vec![0; c]; r];
        let mut answer = 0;
        
        for y in 0..r {
            for x in 0..c {
                if grid[y][x] == 0 {
                    continue;
                }
                visited[y][x] = 1;
                dfs(&grid, &mut visited, x, y, grid[y][x], &mut answer);
                visited[y][x] = 0;
            }
        }
        answer
    }
}