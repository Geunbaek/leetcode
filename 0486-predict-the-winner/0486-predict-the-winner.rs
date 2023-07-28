use std::collections::HashMap;

impl Solution {
    fn max_diff(nums: &Vec<i32>, memo: &mut HashMap<(usize, usize), i32>, left:usize, right: usize) -> i32 {
        if memo.contains_key(&(left, right)) {
            return memo[&(left, right)];
        }
        
        if left == right {
            return nums[left];
        } else {
            let left_score = nums[left] - Solution::max_diff(nums, memo, left + 1, right);
            let right_score = nums[right] - Solution::max_diff(nums, memo, left, right - 1);
            memo.insert((left, right), std::cmp::max(left_score, right_score));
            return memo[&(left, right)];
        }
    }
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut memo:HashMap<(usize, usize), i32> = HashMap::new();
        
        return Solution::max_diff(&nums, &mut memo, 0, n - 1) >= 0;
    }
}
