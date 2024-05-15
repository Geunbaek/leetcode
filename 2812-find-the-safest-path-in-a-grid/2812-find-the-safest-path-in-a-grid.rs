use std::collections::{VecDeque};

impl Solution {
    pub fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {
        fn is_valid(n: usize, grid: &Vec<Vec<i32>>, dist: i32) -> bool {
            if grid[0][0] < dist || grid[n - 1][n - 1] < dist {
                return false;
            }
            
            let dx = [-1, 0, 1, 0];
            let dy = [0, -1, 0, 1];
            
            let mut q: VecDeque<(usize, usize)> = VecDeque::from([(0, 0)]);
            let mut visited = vec![vec![false; n]; n];
            
            visited[0][0] = true;
            
            while let Some((x, y)) = q.pop_front() {
                if x == n - 1 && y == n - 1 {
                    return true;
                }
                
                for i in 0..4 {
                    let nx = (x as i32 + dx[i]) as usize;
                    let ny = (y as i32 + dy[i]) as usize;
                    
                    if !(nx < n && ny < n) {
                        continue;
                    }
                    
                    if visited[ny][nx] {
                        continue;
                    }
                    
                    if grid[ny][nx] < dist {
                        continue;
                    }
                    
                    visited[ny][nx] = true;
                    q.push_back((nx, ny));
                }
            }
            false
        }
        
        
        
        let mut grid = grid.clone();
        let n = grid.len();
        
        let mut q: VecDeque<(usize, usize)> = VecDeque::new();
        
        for y in 0..n {
            for x in 0..n {
                if grid[y][x] == 1 {
                    q.push_back((x, y));
                    grid[y][x] = 0;
                } else {
                    grid[y][x] = -1;
                }
            }
        }
        
        let dx = [-1, 0, 1, 0];
        let dy = [0, -1, 0, 1];
        
        let mut left = 0;
        let mut right = 0;
        let mut answer = -1;
        
        while !q.is_empty() {
            let size = q.len();
            for _ in 0..size {
                match q.pop_front() {
                    Some((x, y)) => {
                        for i in 0..4 {
                            let nx = (x as i32 + dx[i]) as usize;
                            let ny = (y as i32 + dy[i]) as usize;
                            if !(nx < n && ny < n) {
                                continue;
                            }
                            if grid[ny][nx] != -1 {
                                continue;
                            }
                            grid[ny][nx] = grid[y][x] + 1;
                            right = right.max(grid[ny][nx]);
                            q.push_back((nx, ny));
                        }
                    }, 
                    None => {}
                }
            }
        }
 
        while left <= right {
            let mid = left + (right - left) / 2;
            
            if is_valid(n, &grid, mid) {
                left = mid + 1;
                answer = mid;
            } else {
                right = mid - 1;
            }
        }
        answer
    }
}