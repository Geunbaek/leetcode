use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut counter:HashMap<i32, i32> = HashMap::new();
        
        for num in &nums {
            let el = counter.entry(*num).or_insert(0);
            *el += 1;
        }
        
        let mut counter: Vec<_> = counter.iter().collect();
        counter.sort_by_key(|a| a.1);
        
        let mut answer:Vec<i32> = vec![];
        
        for (key, val) in counter.iter().rev() {
            answer.push(**key);
            if answer.len() == k as usize {
                break;
            }
        }
        return answer;
    }
}