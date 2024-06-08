use std::collections::HashMap;

impl Solution {
    pub fn check_subarray_sum(nums: Vec<i32>, k: i32) -> bool {
        let mut cur_mod = 0;
        
        let mut cache: HashMap<i32, i32> = HashMap::from([(0, 0)]);
        
        for (i, num) in nums.iter().enumerate() {
            cur_mod = (cur_mod + num) % k;
            
            if cache.contains_key(&cur_mod) {
                if cache[&cur_mod] < i as i32 {
                    return true;
                } 
            } else {
                cache.insert(cur_mod, (i as i32 + 1));
            }
        }
        false
    }
}