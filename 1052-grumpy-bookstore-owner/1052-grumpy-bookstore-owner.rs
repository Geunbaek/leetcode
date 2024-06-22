impl Solution {
    pub fn max_satisfied(customers: Vec<i32>, grumpy: Vec<i32>, minutes: i32) -> i32 {
        let n = customers.len();
        let mut total = 0;
        let mut dp: Vec<i32> = vec![0];
        let mut max = 0;
        let minutes = minutes as usize;
        
        for (c, g) in customers.iter().zip(&grumpy) {
            let m = dp.len() - 1;
            if *g == 0 {
                total += *c;
                dp.push(dp[m]);
            }
            
            if *g == 1 {
                dp.push(dp[m] + *c);
            }
            
            if m + 1 >= minutes {
                max = std::cmp::max(max, dp[m + 1] - dp[m + 1 - minutes]);
            }
        }
            
        total + max
    }
}