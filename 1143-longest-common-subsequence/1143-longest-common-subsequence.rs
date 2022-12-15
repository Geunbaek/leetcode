use std::cmp;

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let text1:Vec<_> = (String::from(" ") + &text1).chars().collect();
        let text2:Vec<_> = (String::from(" ") + &text2).chars().collect();
        
        let c:usize = text1.len();
        let r:usize = text2.len();
        
        let mut dp: Vec<Vec<i32>> = vec![vec![0; c]; r];
        
        for y in 0..r {
            for x in 0..c {
                if x == 0 || y == 0 {
                    continue;
                }
                
                if text1[x] == text2[y] {
                    dp[y][x] = dp[y - 1][x - 1] + 1;
                } else {
                    dp[y][x] = cmp::max(dp[y - 1][x], dp[y][x - 1]);
                }
            }
        }
        dp[r - 1][c - 1]
    }
}