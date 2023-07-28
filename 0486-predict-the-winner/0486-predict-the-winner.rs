impl Solution {
    fn max_diff(nums: &Vec<i32>, left:usize, right: usize) -> i32 {
        if left == right {
            return nums[left];
        } else {
            let left_score = nums[left] - Solution::max_diff(nums, left + 1, right);
            let right_score = nums[right] - Solution::max_diff(nums, left, right - 1);
            return std::cmp::max(left_score, right_score);
        }
    }
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        let n = nums.len();
        
        return Solution::max_diff(&nums, 0, n - 1) >= 0;
    }
}
