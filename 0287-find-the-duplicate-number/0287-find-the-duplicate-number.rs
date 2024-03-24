impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let n = nums.len() - 1;
        
        let mut cache = vec![0; n + 1];
        
        for num in nums {
            let num = num as usize;
            if cache[num] == 1 {
                return num as i32;
            }
            cache[num as usize] += 1;
        }
        -1
    }
}