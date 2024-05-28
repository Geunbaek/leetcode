impl Solution {
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        let n = s.len();
        
        let mut answer = 0;
        let mut max_cost = max_cost;
        let mut dp = vec![];
        
        for (c1, c2) in s.chars().zip(t.chars()) {
            let a = c1 as u8;
            let b = c2 as u8;
            let cost = a.abs_diff(b) as i32;
            dp.push(cost);
        }
        
        let mut left = 0;
        let mut sum = 0;
        
        for right in 0..n {
            sum += dp[right];
            while left < right && sum > max_cost {
                sum -= dp[left];
                left += 1;
            }
            if sum <= max_cost {
                answer = std::cmp::max(answer, (right - left + 1) as i32);
            }
        }
        answer
    }
}