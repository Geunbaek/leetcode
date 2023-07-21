use std::cmp;

impl Solution {
    pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
        let mut n = nums.len();
        let mut dp: Vec<usize> = vec![1; n];
        let mut count: Vec<usize> = vec![1; n];
        
        for y in 0..n {
            for x in 0..y {
                if nums[y] > nums[x] {
                    if dp[x] + 1 > dp[y] {
                        dp[y] = dp[x] + 1;
                        count[y] = 0;
                    }
                    if dp[x] + 1 == dp[y] {
                        count[y] += count[x];
                    }
                }
            }
        }

        let max = *dp.iter().max().unwrap();
        let mut answer = 0;
        
        for i in 0..n {
            if dp[i] == max {
                answer += count[i] as i32;
            }
        }
        return answer;
    }
}
