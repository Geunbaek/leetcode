impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut result = 0;
        
        for num in nums {
            result |= num;
        }
        
        result << (n - 1)     
    }
}