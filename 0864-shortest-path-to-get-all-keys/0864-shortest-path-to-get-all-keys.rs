use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn shortest_path_all_keys(grid: Vec<String>) -> i32 {
        let r = grid.len();
        let c = grid[0].len();
        
        let mut q: VecDeque<(usize, usize, usize, usize)> = VecDeque::new();
        let mut board:Vec<Vec<char>> = vec![vec![]; r];
        let mut all_keys:usize = 0;
        let mut visited: Vec<HashSet<(usize, usize)>> = vec![HashSet::new(); 64];
        let dx = [-1, 0, 1, 0];
        let dy = [0, -1, 0, 1];
        
        for y in 0..r {
            board[y] = grid[y].chars().collect::<Vec<char>>();
            for x in 0..c {
                let cell = board[y][x];
                if cell == '@' {
                    q.push_back((x, y, 0, 0));
                    visited[0].insert((x, y));
                    board[y][x] = '.';
                } else if cell.is_lowercase() {
                    all_keys += (1 << (cell as u8 - 'a' as u8));
                }
            }
        }
        
        while let Some((x, y, keys, dist)) = q.pop_front() {
            if keys == all_keys {
                return dist as i32;
            }
            for i in 0..4 {
                let nx = (x as isize + dx[i]) as usize;
                let ny = (y as isize + dy[i]) as usize;
                
                if !(0 <= nx && nx < c && 0 <= ny && ny < r) {
                    continue;
                }
                
                if board[ny][nx] == '#' {
                    continue;
                }
                
                if visited[keys].contains(&(nx, ny)) {
                    continue;
                }
                
                if board[ny][nx] == '.' {
                    visited[keys].insert((nx, ny));
                    q.push_back((nx, ny, keys, dist + 1));
                } else if board[ny][nx].is_lowercase() {
                    let cell = board[ny][nx];
                    let new_keys = keys | (1 << (cell as u8 - 'a' as u8));
                    visited[new_keys].insert((nx, ny));
                    q.push_back((nx, ny, new_keys, dist + 1));
                } else {
                    let cell = board[ny][nx];
                    
                    if keys & (1 << (cell as u8 - 'A' as u8)) == 0 {
                        continue;
                    }
                    visited[keys].insert((nx, ny));
                    q.push_back((nx, ny, keys, dist + 1));
                }
                
            }
       
        }
        return -1;
    }
}