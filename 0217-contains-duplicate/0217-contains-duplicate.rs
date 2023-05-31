use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let set:HashSet<&i32> = nums.iter().collect();
        return set.len() != nums.len();
    }
}