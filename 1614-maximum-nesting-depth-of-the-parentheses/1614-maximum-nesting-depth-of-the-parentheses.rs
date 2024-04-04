impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        
        let mut depth = 0;
        let mut max = 0;
        for c in s {
            if c == '(' {
                depth += 1;
            }
            if c == ')' {
                depth -= 1;
            }
            max = std::cmp::max(max, depth);
        }
        max
    }
}