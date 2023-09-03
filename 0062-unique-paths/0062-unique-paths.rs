impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {    
        let m = m as usize;
        let n = n as usize;
        let mut dp = vec![vec![0; m + 1]; n + 1];
        dp[1][1] = 1;
        
        for y in 1..=n {
            for x in 1..=m {
                dp[y][x] = std::cmp::max(dp[y][x], dp[y - 1][x] + dp[y][x - 1]);
            }
        }
      
        return dp[n][m];
    }
}