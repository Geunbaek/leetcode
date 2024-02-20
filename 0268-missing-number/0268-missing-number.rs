impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut nums = nums.clone();
        nums.sort();
        for (i, num) in nums.iter().enumerate() {
            if i as i32 != *num {
                return i as i32;
            }
        }
        nums.len() as i32
    }
}