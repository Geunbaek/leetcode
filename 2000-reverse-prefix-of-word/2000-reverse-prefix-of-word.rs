impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
        let n = word.len();
        let mut first_char_index = 0;
        let word: Vec<String> = word.chars().map(|x| x.to_string()).collect(); 
        
        for (i, c) in word.iter().enumerate() {
            if *c == ch.to_string() {
                first_char_index = i;
                break;
            }
        } 
        
        let mut ret = String::new();
        
        for i in 0..=first_char_index {
            ret.push_str(&word[first_char_index - i]);
        }
        
        for i in first_char_index + 1..n {
            ret.push_str(&word[i]);
        }
        
        ret
    }
}