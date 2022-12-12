impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        let N: usize = n as usize;
        
        let mut dp: Vec<i32> = vec![0; N + 1];
        dp[0] = 1;
        dp[1] = 1;
        
        for i in 2..=N {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        dp[N]
    }
}