impl Solution {
    pub fn get_averages(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let mut answer = vec![-1; n];
        let count = (2 * k + 1) as i32;
        
        if k == 0 {
            return nums;
        }
        
        if count as usize > n {
            return answer;
        }
        
        let mut prefix_sum: Vec<i64> = vec![0; n + 1];
        
        for i in 0..n {
            prefix_sum[i + 1] = prefix_sum[i] + nums[i] as i64;
        }
        
        for i in k..n-k {
            answer[i] = ((prefix_sum[i + k + 1] - prefix_sum[i - k]) / count as i64) as i32;
        }
        return answer;
    }
}