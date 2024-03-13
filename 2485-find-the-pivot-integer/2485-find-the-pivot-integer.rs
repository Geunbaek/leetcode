impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let (mut left, mut right) = (0, (1..=n).sum::<i32>());
        for i in 1..=n {
            left += i;
            
            if left == right {
                return i;
            }
            right -= i;
        }
        return -1;
    }
}