impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let r = obstacle_grid.len();
        let c = obstacle_grid[0].len();
        
        
        let mut dp: Vec<Vec<i32>> = vec![vec![0; c + 1]; r + 1];
        
        if obstacle_grid[0][0] == 0 {
            dp[1][1] = 1;
        }
        
        for y in 1..=r {
            for x in 1..=c {
                if obstacle_grid[y - 1][x - 1] == 1 {
                    continue;
                }
                if x == 1 && y == 1 {
                    continue;
                }
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1];
            }
        }

        return dp[r][c];
    }
}