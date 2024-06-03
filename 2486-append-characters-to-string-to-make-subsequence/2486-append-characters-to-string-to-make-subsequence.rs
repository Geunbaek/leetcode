impl Solution {
    pub fn append_characters(s: String, t: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();
        
        let mut left = 0;
        let mut max = 0;
        
        let n = s.len();
        let m = t.len();
        
        while left < n && max < m {
            if s[left] == t[max] {
                max += 1;
            }
            left += 1;
        }
        (m - max) as i32
    }
}