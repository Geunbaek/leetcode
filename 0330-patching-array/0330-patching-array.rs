use std::collections::HashSet;

impl Solution {
    pub fn min_patches(nums: Vec<i32>, n: i32) -> i32 {
        let mut patches = 0;
        
        let mut i = 0;
        let mut miss = 1_isize;
        
        while miss <= n as isize {
            if i < nums.len() && nums[i] as isize <= miss {
                miss += nums[i] as isize;
                i += 1;
            } else {
                miss += miss;
                patches += 1;
            }
        }
        patches
    }
}