use std::cmp;

impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut prefix: Vec<usize> = vec![0];
        let target = target as usize;
        
        let n = nums.len();
        
        for i in 0..n {
            prefix.push(prefix[i] + nums[i] as usize);
        }
        
        let mut right: usize = 0;
        let mut answer: usize = usize::MAX;
        
        for left in 0..n {
            while right < n + 1 && prefix[right] - prefix[left] < target {
                right += 1;
            }
            if right < n + 1 && prefix[right] - prefix[left] >= target {
                answer = cmp::min(answer, right - left);
            }
        }
        
        match answer {
            usize::MAX => 0,
            _ => answer as i32,
        }
    }
}