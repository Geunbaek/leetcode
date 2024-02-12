use std::collections::HashMap;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut counter:HashMap<i32, usize> = HashMap::new();
        
        for num in nums.iter() {
            counter.entry(*num).and_modify(|x| *x += 1).or_insert(1);
            if counter[num] as f64 >= n as f64 / 2.0 {
                return *num;
            }
        }
        
        return -1;
    }
}