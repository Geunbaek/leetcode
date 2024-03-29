use std::collections::HashMap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut left = 0_usize;
        let mut answer = 0;
        let mut cache: HashMap<i32, i32> = HashMap::new();
        let max = nums.iter().max().unwrap();
        
        for right in 0..n {
            cache.entry(nums[right]).and_modify(|x| *x += 1).or_insert(1);
            
            while left <= right && cache.contains_key(max) && cache[&max] == k {
                cache.entry(nums[left]).and_modify(|x| *x -= 1).or_insert(1);
                left += 1;
            }
            answer += left;
        }
        answer as i64
    }
}