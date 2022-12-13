use std::cmp;

impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        let r:usize = matrix.len();
        let c:usize = matrix[0].len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; c]; r];
        
        for i in 0..c {
            dp[0][i] = matrix[0][i];
        }
        
        for y in 1..r {
            for x in 0..c {
                if x == 0 {
                    dp[y][x] = cmp::min(dp[y - 1][x], dp[y - 1][x + 1]) + matrix[y][x];
                } else if x == c - 1 {
                    dp[y][x] = cmp::min(dp[y - 1][x], dp[y - 1][x - 1]) + matrix[y][x];
                } else {
                    dp[y][x] = cmp::min(dp[y - 1][x], cmp::min(dp[y - 1][x - 1], dp[y - 1][x + 1])) + matrix[y][x];
                }
            }
        }
        let mut answer = 10001;
        
        for i in 0..c {
            answer = cmp::min(answer, dp[r - 1][i]);
        }
        answer
    }
}