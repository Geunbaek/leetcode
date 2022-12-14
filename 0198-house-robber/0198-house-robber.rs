use std::cmp;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n: usize = nums.len();
        
        if n == 1 {
            return nums[0];
        } 
        
        if n == 2 {
            return cmp::max(nums[0], nums[1]);
        }
        
        let mut dp: Vec<i32> = vec![0; n];
        dp[0] = nums[0];
        dp[1] = nums[1];
     
        let mut max = cmp::max(dp[0], dp[1]);
        
        for i in 2..n {
            if i < 3 {
                dp[i] = dp[i - 2] + nums[i];
            } else {
                dp[i] = cmp::max(dp[i - 2], dp[i - 3]) + nums[i];
            }

            max = cmp::max(max, dp[i]);
        }
        max
    }
}