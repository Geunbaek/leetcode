impl Solution {
    pub fn minimum_replacement(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut nums = nums;
        let mut answer = 0_i64;
        if n == 1 {
            return 0;
        }
        for i in (0..=n-2).rev() {
            if nums[i + 1] >= nums[i] {
                continue;
            }
            let el =  (nums[i] + nums[i + 1] - 1) / nums[i + 1];
            answer += (el - 1) as i64;
            nums[i] = nums[i] / el;
            
        }
        return answer;
    }
}