use std::{collections::HashMap, cmp};

impl Solution {
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        fn dp(
            grid: &Vec<Vec<i32>>,
            memo: &mut HashMap<(usize, usize, usize), i32>, 
            r: usize, 
            c: usize, 
            row: usize, 
            col1: usize, 
            col2: usize
        ) -> i32 {
            if row >= r {
                return 0;
            }
            
            if !(col1 < c && col2 < c) {
                return 0;
            }
            
            if memo.contains_key(&(row, col1, col2)) {
                return memo[&(row, col1, col2)];
            }
            
            let mut ret = grid[row][col1];
            
            if col1 != col2 {
                ret += grid[row][col2];
            }
            
            let next_col1_arr: Vec<usize> = {
                if col1 == 0 {
                    vec![col1, col1 + 1]
                } else if col1 == c - 1 {
                    vec![col1 - 1, col1]
                } else {
                    vec![col1 - 1, col1, col1 + 1]
                }
            };
            
            let next_col2_arr: Vec<usize> = {
                if col2 == 0 {
                    vec![col2, col2 + 1]
                } else if col2 == c - 1 {
                    vec![col2 - 1, col2]
                } else {
                    vec![col2 - 1, col2, col2 + 1]
                }
            };
            
            let mut max = 0;
            for next_col1 in next_col1_arr.iter() {
                for next_col2 in next_col2_arr.iter() {
                    max = cmp::max(max, dp(
                        grid,
                        memo, 
                        r, 
                        c, 
                        row + 1, 
                        *next_col1, 
                        *next_col2
                    ));
                }
            }
            ret += max;
            
            memo.insert((row, col1, col2), ret);
            
            return ret;
            
        }
        
        let (r, c) = (grid.len(), grid[0].len());
        let mut memo: HashMap<(usize, usize, usize), i32> = HashMap::new();
        
        return dp(
            &grid, 
            &mut memo, 
            r, 
            c, 
            0, 
            0, 
            c - 1
        );
        
    }
}