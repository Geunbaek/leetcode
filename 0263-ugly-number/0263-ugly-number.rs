impl Solution {
    pub fn is_ugly(n: i32) -> bool {
        if n < 1 {
            return false;
        }
        
        if n == 1 || n == 2 || n == 3 || n == 5 {
            return true;
        }
        
        if n % 2 == 0 {
            return Solution::is_ugly(n / 2);
        } else if n % 3 == 0 {
            return Solution::is_ugly(n / 3);
        } else if n % 5 == 0 {
            return Solution::is_ugly(n / 5);
        }
        
        return false
    }
}