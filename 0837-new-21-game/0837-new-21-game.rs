impl Solution {
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        let n:usize = n as usize;
        let k: usize = k as usize;
        let max_pts: usize = max_pts as usize;
        let mut dp: Vec<f64> = vec![0.0; n + 1];
        dp[0] = 1.0;
        
        for i in 1..n + 1 {
            for j in 1..max_pts + 1 {
                if i - j >= 0 && i - j < k {
                    dp[i] += dp[(i - j)] / max_pts as f64;
                }
            }
        }
        let mut answer:f64 = 0.0;
        
        for i in k..n+1 {
            answer += dp[i];
        }
        return answer
    }
}