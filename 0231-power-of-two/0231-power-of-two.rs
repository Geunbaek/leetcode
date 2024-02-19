impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        
        if n == 1 {
            return true;
        }
        
        let mut n = n;
        
        while n >= 2 {
            if n % 2 == 0 {
                n /= 2;
            } else {
                return false;
            }
        }
        return true;
    }
}