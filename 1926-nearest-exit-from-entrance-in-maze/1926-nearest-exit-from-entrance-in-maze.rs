use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn nearest_exit(maze: Vec<Vec<char>>, entrance: Vec<i32>) -> i32 {
        let mut maze = maze;
        let mut q = VecDeque::new();
        q.push_back((entrance[1] as usize, entrance[0] as usize, 0 as usize));
        maze[entrance[0] as usize][entrance[1] as usize] = '@';
        
        let dx: [isize; 4] = [-1, 0, 1, 0];
        let dy: [isize; 4] = [0, -1, 0, 1];
        
        while !q.is_empty() {
            while let Some((x, y, cnt)) = q.pop_front() {
                if cnt != 0 && (x == 0 || y == 0 || y == maze.len() - 1 || x == maze[0].len() - 1) {
                    return cnt as i32;
                }
                for i in 0..4 {
                    let nx = (x as isize + dx[i]) as usize;
                    let ny = (y as isize + dy[i]) as usize;

                    if nx >= maze[0].len() || nx < 0 || ny >= maze.len() || ny < 0 {
                        continue;
                    }

                    if maze[ny][nx] == '+' || maze[ny][nx] == '@' {
                        continue;
                    }
                    maze[ny][nx] ='@';
                    q.push_back((nx, ny, cnt + 1));
                }
           
            }
        }
        -1
    }
}