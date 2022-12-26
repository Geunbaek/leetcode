use std::cmp;

impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut max_len: i32 = 0;
        
        for (i, num) in nums.iter().enumerate() {
            if max_len < i as i32 {
                return false;
            }
            max_len = cmp::max(max_len, i as i32 + num);
        }
        true
    }
}