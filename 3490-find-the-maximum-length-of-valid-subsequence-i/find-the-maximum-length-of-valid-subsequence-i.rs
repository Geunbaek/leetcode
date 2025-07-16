use std::cmp;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let mut even = 0;
        let mut odd = 0;
        let mut assemble = 0;
        let mut assemble_last = 0;

        for num in &nums {
            if num % 2 == 0 {
                even += 1;
                
                if assemble == 0 {
                    assemble += 1;
                    assemble_last = *num;
                    continue;
                } 

                if assemble_last % 2 != 0 {
                    assemble += 1;
                    assemble_last = *num;
                }
  
            } else {
                odd += 1;
                if assemble == 0 {
                    assemble += 1;
                    assemble_last = *num;
                    continue;
                } 

                if assemble_last % 2 == 0 {
                    assemble += 1;
                    assemble_last = *num;
                }
            }
        }

        cmp::max(cmp::max(even, odd), assemble) 
    }
}
