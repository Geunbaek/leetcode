use std::collections::HashMap;

impl Solution {
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        let n = nums.len();
        let mut sum = 0;
        let mut answer = 0;
        let mut cache: HashMap<i32, i32> = HashMap::new();
        
        for i in 0..n {
            sum += nums[i];
            
            if sum == goal {
                answer += 1;
            }
            
            if cache.contains_key(&(sum - goal)) {
                answer += cache[&(sum - goal)];
            }
            
            cache.entry(sum).and_modify(|x| *x += 1).or_insert(1);
        }
        answer
    }
}