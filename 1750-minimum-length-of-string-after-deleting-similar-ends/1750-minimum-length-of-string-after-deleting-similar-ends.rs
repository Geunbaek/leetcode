impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        let vec_s:Vec<char> = s.chars().collect();
        
        let n = s.len();
        
        let (mut left, mut right) = (0_usize, n - 1);
        
        while left < right {
            if vec_s[left] != vec_s[right] {
                break;
            }
            
            let target = vec_s[left];
            
            while left <= right && vec_s[left] == target {
                left += 1;
            }
            
            while left <= right && vec_s[right] == target {
                right -= 1;
            }
        }
    
        return (right - left + 1) as i32;
    }
}