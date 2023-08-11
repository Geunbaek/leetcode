impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        let amount = amount as usize;
        let n = coins.len();
        let mut dp:Vec<Vec<usize>> = vec![vec![0; amount + 1]; n + 1];
        
        for y in 0..=n {
            dp[y][0] = 1;
        }

        for (y, coin) in coins.iter().enumerate() {
            for x in 0..=amount {
                if x < *coin as usize {
                    dp[y + 1][x] = dp[y][x];
                } else {
                    dp[y + 1][x] = dp[y][x] + dp[y + 1][x - *coin as usize];
                }
            }
        }

        return dp[n][amount] as i32;
    }
}