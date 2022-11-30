use std::collections::{HashSet, HashMap};

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut counter = HashMap::new();
        let mut count_set = HashSet::new();
        
        for num in arr {
            let count = counter.entry(num).or_insert(0);
            *count += 1;
        }
        
        for (key, val) in counter {
            if count_set.contains(&val) {
                return false;
            }
            count_set.insert(val);
        }
        true
    }
}