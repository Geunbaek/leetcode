impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        if k == 0 {
            return 0;
        }
        
        let mut left = 0;
        let mut prod = 1;
        let mut answer = 0;
        
        for (right, num) in nums.iter().enumerate() {
            prod *= num;
            while left <= right && prod >= k {
                prod /= nums[left];
                left += 1;
            }
            
            answer += right - left + 1;
        }
        answer as i32
    }
}
