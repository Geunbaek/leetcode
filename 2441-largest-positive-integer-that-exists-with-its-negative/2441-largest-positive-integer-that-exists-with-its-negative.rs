use std::collections::HashMap;

impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        let mut max = -1;
        let mut cache: HashMap<i32, i32> = HashMap::new();
        for num in nums.iter() {
            if cache.contains_key(&-num) {
                if *num > 0 {
                    max = std::cmp::max(max, *num);
                } else {
                    max = std::cmp::max(max, -*num);
                }
            }
            cache.entry(*num).and_modify(|x| *x += 1).or_insert(1);
            
        }
        max
    }
}