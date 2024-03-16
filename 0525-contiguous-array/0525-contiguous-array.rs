use std::{cmp, collections::HashMap};

impl Solution {
    pub fn find_max_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp: Vec<i32> = vec![0];
        let mut cache: HashMap<i32, usize> = HashMap::new();
        let mut answer = 0;
        
        cache.insert(0, 0);
        
        for right in 0..n {
            let next = {
                if nums[right] == 1 {
                    dp[right] + 1
                } else {
                    dp[right] - 1
                }
            };
            dp.push(next);
            
            let left = cache.entry(next).or_insert(right + 1);
            answer = cmp::max(answer, right + 1 - *left);
            
        }
        (answer) as i32
    }
}