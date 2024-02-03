use std::cmp::{ max, min };

impl Solution {
    pub fn max_sum_after_partitioning(arr: Vec<i32>, k: i32) -> i32 {
        let n = arr.len();
        let mut dp: Vec<i32> = vec![0; n + 1];
        
        for i in 1..n + 1 {
            let mut _max = 0;
            
            for j in 1..min(k as usize, i) + 1 {
                _max = max(_max, arr[i - j]);
                dp[i] = max(dp[i], dp[i - j] + _max * j as i32);
            }
        }
        dp[n]
    }
}