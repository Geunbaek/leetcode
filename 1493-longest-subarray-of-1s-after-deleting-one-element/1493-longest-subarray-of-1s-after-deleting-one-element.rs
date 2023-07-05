use std::cmp;

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let n:usize = nums.len();
        
        let mut prefix_sum = vec![0; n + 1];
        for i in 1..=n {
            if nums[i - 1] == 1 {
                prefix_sum[i] = prefix_sum[i - 1];
            } else {
                prefix_sum[i] = prefix_sum[i - 1] + 1;
            }
        }
        let mut left:usize = 0;
        let mut right:usize = 1;
        let mut answer:usize = 0;
        
        while right <= n {
            while right <= n && prefix_sum[right] - prefix_sum[left] <= 1 {
                right += 1;
            } 
            answer = cmp::max(answer, right - left - 2);
            left += 1;
            
        }
        return answer as i32;
    }
}