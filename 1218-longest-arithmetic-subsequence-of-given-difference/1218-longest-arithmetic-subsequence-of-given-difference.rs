use std::collections::HashMap;
use std::cmp;

impl Solution {
    pub fn longest_subsequence(arr: Vec<i32>, difference: i32) -> i32 {
        let mut cache:HashMap<i32, i32> = HashMap::new();
        let mut answer: i32 = 0;
        
        for num in arr.iter() {
            if cache.contains_key(&(*num - difference)) {
                cache.insert(*num, *cache.get(&(*num - difference)).unwrap() + 1);
            } else {
                cache.insert(*num, 1);
            }
            answer = cmp::max(answer, *cache.get(num).unwrap());
        }

        return answer;
    }
}