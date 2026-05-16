impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let min_value = nums.iter().min();
        match min_value {
            Some(min) => return *min,
            None => return -1,
        }
    }
}