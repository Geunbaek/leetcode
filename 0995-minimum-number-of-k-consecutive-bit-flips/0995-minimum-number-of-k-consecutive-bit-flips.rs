impl Solution {
    pub fn min_k_bit_flips(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let n = nums.len();
        
        let mut count = 0;
        let mut isFlip = vec![false; n];
        let mut flipCount = 0;
        
        for i in 0..n {    
            if i >= k {
                if isFlip[i - k] {
                    flipCount -= 1;
                }
            }
            
            if flipCount % 2 == nums[i] {
                if i + k > n {
                    return -1;
                }
                flipCount += 1;
                count += 1;
                isFlip[i] = true;
            }
        }
        count
    }
}