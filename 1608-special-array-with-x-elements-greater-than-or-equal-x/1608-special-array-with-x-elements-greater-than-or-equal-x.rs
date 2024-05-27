impl Solution {
    pub fn special_array(nums: Vec<i32>) -> i32 {
        for i in 1..=1000 {
            let mut count = 0;
            for num in nums.iter() {
                if *num >= i {
                    count += 1;
                }
            }
            if count == i {
                return i;
            }
        }
        return -1;
    }
}