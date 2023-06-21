use std::cmp;

impl Solution {
    pub fn get_cost(nums: &Vec<i32>, cost: &Vec<i32>, target:usize) -> i64 {
        let mut sum:i64 = 0;
        for (n, c) in nums.iter().zip(cost.iter()) {
            sum += ((target as i64 - *n as i64).abs() * *c as i64);
        }
        return sum;
    }
    
    pub fn min_cost(nums: Vec<i32>, cost: Vec<i32>) -> i64 { 
        let (mut left, mut right):(usize, usize) = (0, 1000001);
        let mut answer: i64 = 0;
        
        while left <= right {
            let mid = left + (right - left) / 2;
            
            let cost1 = Solution::get_cost(&nums, &cost, mid);
            let cost2 = Solution::get_cost(&nums, &cost, mid + 1);
            answer = cmp::min(cost1, cost2);
            
            if cost1 > cost2 {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return answer;
    }
}