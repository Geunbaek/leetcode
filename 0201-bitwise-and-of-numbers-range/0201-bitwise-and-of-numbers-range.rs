impl Solution {
    pub fn range_bitwise_and(left: i32, right: i32) -> i32 {
        let mut count = 0;
        let mut left = left;
        let mut right = right;
        
        while right != left {
            right >>= 1;
            left >>= 1;
            count += 1;
        }
        
        return left << count;
    }
}