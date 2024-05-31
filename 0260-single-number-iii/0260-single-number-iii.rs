use std::collections::HashMap;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let mut cache: HashMap<i32, i32> = HashMap::new();
        let mut answer = vec![];
        
        for num in nums {
            cache.entry(num).and_modify(|x| *x -= 1).or_insert(1);
        }
        
        for (num, count) in cache.iter() {
            if *count == 1 {
                answer.push(*num);
            }    
        }
        answer
    }
}