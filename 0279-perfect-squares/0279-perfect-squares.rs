use std::cmp;

impl Solution {
    pub fn num_squares(n: i32) -> i32 {
        let max = u32::MAX;
        let mut dp = vec![max; n as usize + 1];
        dp[0] = 0;
        
        for num in 1..((n as f64).sqrt() as usize + 1){
            for i in num.pow(2)..(n as usize + 1) {
                dp[i] = cmp::min(dp[i], dp[i - num.pow(2)] + 1)
            }
        }
        dp[n as usize] as i32
    }
}       
        