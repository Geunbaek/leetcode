impl Solution {
    pub fn valid_partition(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut dp: Vec<bool> = vec![false; n + 1];
        dp[0] = true;
        
        for i in 2..n + 1 {
            if dp[i - 2] {
                if nums[i - 1] == nums[i - 2] {
                    dp[i] = true;
                }
            }
            
            if i >= 3 && dp[i - 3] {
                if nums[i - 1] == nums[i - 2] && nums[i - 1] == nums[i - 3] {
                    dp[i] = true;
                }
    
                if nums[i -1] == nums[i - 2] + 1 && nums[i - 1] == nums[i - 3] + 2 {
                    dp[i] = true;
                }
            }
        }
        dp[n]
    }
}
