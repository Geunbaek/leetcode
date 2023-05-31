use std::{cmp, collections::{VecDeque}};

impl Solution {
    pub fn find_max_fish(grid: Vec<Vec<i32>>) -> i32 {

        fn bfs(grid: &Vec<Vec<i32>>, visited:&mut Vec<Vec<i32>> ,x: usize, y: usize) -> i32 {
            let (r, c) = (grid.len(), grid[0].len());
            let mut q = VecDeque::from([(x, y)]);
            visited[y][x] = 1;
            let mut fish_count:i32 = 0;
            let dx = [-1, 0, 1, 0];
            let dy = [0, -1, 0, 1];

            while let Some((x, y)) = q.pop_front() {
                fish_count += grid[y][x];
                for i in 0..4 {
                    let nx = (x as isize + dx[i]) as usize;
                    let ny = (y as isize + dy[i]) as usize;
                    if !(0 <= nx && nx < c && 0 <= ny && ny < r) {
                        continue;
                    }
                    if visited[ny][nx] == 1 {
                        continue;
                    }
                    if grid[ny][nx] == 0 {
                        continue;
                    }
                    visited[ny][nx] = 1;
                    q.push_back((nx, ny));
                }
            }
            return fish_count;
        }

        let (r, c) = (grid.len(), grid[0].len());
        let mut visited:Vec<Vec<i32>> = vec![vec![0; c]; r];
        let mut answer:i32 = 0;

        for y in 0..r {
            for x in 0..c {
                if grid[y][x] == 0 || visited[y][x] == 1 {
                    continue;
                }
                let fish_count = bfs(&grid, &mut visited, x, y);
                answer = cmp::max(answer, fish_count);
            }
        }
        return answer;
    }
}