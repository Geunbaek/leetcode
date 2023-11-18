
impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = Vec::from(nums);
        nums.sort();
        let n = nums.len();
        let k = k as usize;
    
        let mut answer:usize = 0;
        let mut left: usize = 0;
        let mut sum:usize = 0;
        
        for right in 0..n {
            let target = nums[right] as usize;
            sum += target;
            while left <= right && (right - left + 1) * target - sum > k {
                sum -= nums[left] as usize;
                left += 1;
            }
            
            answer = std::cmp::max(answer, right - left + 1);
        }
        answer as i32
    }
}