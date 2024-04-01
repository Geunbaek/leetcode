impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let ss:Vec<&str> = s.split_whitespace().collect();
        let n = ss.len();
        ss[n - 1].len() as i32
    }
}