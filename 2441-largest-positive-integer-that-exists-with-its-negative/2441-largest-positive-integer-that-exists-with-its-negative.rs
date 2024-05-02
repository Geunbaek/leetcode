impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        let mut max = -1;
        
        for num in nums.iter() {
            if nums.contains(&-num) {
                if *num > 0 {
                    max = std::cmp::max(max, *num);
                } else {
                    max = std::cmp::max(max, -*num);
                }
            }
        }
        max
    }
}