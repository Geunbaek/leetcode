impl Solution {
    pub fn min_increment_for_unique(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        
        let mut nums = nums.clone();
        nums.sort();
        
        let mut answer = 0;
        
        for i in 1..n {
            if nums[i] <= nums[i - 1] {
                answer += nums[i - 1] + 1 - nums[i];
                nums[i] = nums[i - 1] + 1
            }
        }
        answer
    }
}