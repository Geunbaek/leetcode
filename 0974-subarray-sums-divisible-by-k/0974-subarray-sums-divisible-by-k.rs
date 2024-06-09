use std::collections::HashMap;

impl Solution {
    pub fn subarrays_div_by_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut cache: HashMap<i32, i32> = HashMap::new();
        
        cache.insert(0, 1);
        
        let mut sum = 0;
        let mut answer = 0;
        
        for num in nums {
            sum = (sum + num % k + k) % k;
            if cache.contains_key(&sum) {
                answer += cache[&sum];
            }
            cache.entry(sum).and_modify(|x| *x += 1).or_insert(1);         
        }
        answer
    }
}
