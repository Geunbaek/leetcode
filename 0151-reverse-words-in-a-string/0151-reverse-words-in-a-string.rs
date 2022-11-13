impl Solution {
    pub fn reverse_words(s: String) -> String {
        let _splited_s: Vec<_> = s.trim().split(" ").filter(|&sub_string| *sub_string != String::new()).map(|sub_string| sub_string.trim()).collect();
        let reversed_s: Vec<_> = _splited_s.into_iter().rev().collect();
        return reversed_s.join(" ");
    }
}