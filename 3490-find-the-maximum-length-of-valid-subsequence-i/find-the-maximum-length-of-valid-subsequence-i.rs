use std::cmp;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let mut evens: Vec<i32> = vec![];
        let mut odds: Vec<i32> = vec![];
        let mut assemble: Vec<i32> = vec![];

        for num in &nums {
            if num % 2 == 0 {
                evens.push(*num);
                
                if assemble.len() == 0 {
                    assemble.push(*num);
                } else {
                    if assemble[assemble.len() - 1] % 2 != 0 {
                        assemble.push(*num);
                    }
                }
            } else {
                odds.push(*num);
                if assemble.len() == 0 {
                    assemble.push(*num);
                } else {
                    if assemble[assemble.len() - 1] % 2 == 0 {
                        assemble.push(*num);
                    }
                }
            }
        }

        cmp::max(cmp::max(
            evens.len(), odds.len()
        ), assemble.len()) as i32
    }
}
