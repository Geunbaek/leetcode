impl Solution {
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        let mut nums = nums.clone();
        let mut min = 1;
        
        nums.sort();
        
        for num in nums {
            if num <= 0 {
                continue;
            }
            
            if min < num {
                return min;
            }
            
            if min == num {
                min += 1;
            }
        }
        return min;
    }
}