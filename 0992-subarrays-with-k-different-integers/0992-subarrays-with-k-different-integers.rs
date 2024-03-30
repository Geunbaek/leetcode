use std::collections::HashMap;

impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut k = k;
        
        let mut cache: HashMap<i32, i32> = HashMap::new();
        
        let mut left = 0_usize;
        let mut right = 0_usize;
        let mut total = 0;
        let mut current = 0;
        
        while right < n {
            cache.entry(nums[right]).and_modify(|x| *x += 1).or_insert(1);
            if cache[&nums[right]] == 1 {
                k -= 1;
            }
            
            if k < 0 {
                cache.entry(nums[left]).and_modify(|x| *x -= 1);
                if cache[&nums[left]] == 0 {
                    k += 1
                }
                left += 1;
                current = 0;
            }
            if k == 0 {
                while cache[&nums[left]] > 1 {
                    cache.entry(nums[left]).and_modify(|x| *x -= 1);
                    left += 1;
                    current += 1;
                }
                total += (current + 1);
            }
            right += 1
        }
        
        total as i32
    }
}