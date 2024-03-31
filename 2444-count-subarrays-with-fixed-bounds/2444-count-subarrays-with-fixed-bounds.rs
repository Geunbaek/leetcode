use std::collections::{HashMap, BinaryHeap};

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut answer = 0;
        
        let (mut min_k_index, mut max_k_index, mut left_bound) = (-1, -1, -1);
        
        for (i, num) in nums.into_iter().enumerate(){
            if num < min_k || num > max_k {
                left_bound = i as i32;
            }
                
            if num == min_k {
                min_k_index = i as i32;
            }
            if num == max_k {
                max_k_index = i as i32;
            }
                
            answer += (std::cmp::max(0, std::cmp::min(min_k_index, max_k_index) - left_bound)) as i64;
        }

        return answer;
    }
}