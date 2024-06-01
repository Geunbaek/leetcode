impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let mut answer = 0;
        let s: Vec<char> = s.chars().collect();
        let n = s.len();
        
        for i in 0..n - 1 {
            answer += (s[i] as u8 as i32).abs_diff(s[i + 1] as u8 as i32) as i32;
        }
        answer
    }
}