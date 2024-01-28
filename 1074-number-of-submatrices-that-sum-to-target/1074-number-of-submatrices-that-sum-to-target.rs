use std::collections::HashMap;

impl Solution {
    pub fn num_submatrix_sum_target(matrix: Vec<Vec<i32>>, target: i32) -> i32 {
        let (r, c) = (matrix.len(), matrix[0].len());
        let mut ans = 0;
        let mut dp: Vec<Vec<isize>> = vec![vec![0; c + 1]; r + 1];
        
        for y in 1..=r {
            for x in 1..=c {
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1] - dp[y - 1][x - 1] + matrix[y - 1][x - 1] as isize;
            }
        }
        
        for y1 in 1..=r {
            for y2 in y1..=r {
                let mut cache: HashMap<isize, isize> = HashMap::new();
                cache.insert(0, 1);
                for col in 1..=c {
                    let sub_sum = dp[y2][col] - dp[y1 - 1][col];
                    
                    match cache.get(&(sub_sum - target as isize)) {
                        Some(count) => {
                            ans += count;
                        }
                        None => {}
                    }
                    cache.entry(sub_sum).and_modify(|counter| *counter += 1).or_insert(1);
                }

            }
        }
        
        ans as i32
    }
}