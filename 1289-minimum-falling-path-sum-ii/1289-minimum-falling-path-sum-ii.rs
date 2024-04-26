impl Solution {
    pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let (r, c) = (grid.len(), grid[0].len());
        
        let mut dp: Vec<Vec<i32>> = vec![vec![20000; c]; r];
        
        for y in 0..r {
            for x in 0..c {
                if y == 0 {
                    dp[y][x] = grid[y][x];
                    continue;
                }
                
                for i in 0..c {
                    if x == i {
                        continue;
                    }
                    dp[y][x] = std::cmp::min(dp[y][x], dp[y - 1][i] + grid[y][x])
                }
            }
        }
        *dp.last().unwrap().iter().min().unwrap()
    }
}