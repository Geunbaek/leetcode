use std::collections::HashMap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut cache: HashMap<i32, i32> = HashMap::new();
        let mut answer = 0; 
        let mut left = 0;
        
        for right in 0..n {
            let num = nums[right];
            cache.entry(num).and_modify(|x| *x += 1).or_insert(1);
            
            while left <= right && cache[&num] > k {
                let l_num = nums[left];
                left += 1;
                cache.entry(l_num).and_modify(|x| *x -= 1).or_insert(1);
            }
            
            answer = std::cmp::max(answer, right - left + 1);
        }
        answer as i32
    }
}