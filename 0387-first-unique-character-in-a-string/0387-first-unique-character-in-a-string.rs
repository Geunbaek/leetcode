use std::collections::HashMap;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut counter: HashMap<char, i32> = HashMap::new();
        for c in s.chars() {
            counter.entry(c).and_modify(|x| *x += 1).or_insert(1);
        }
        
        for (i, c) in s.chars().enumerate() {
            if counter[&c] == 1 {
                return i as i32;
            }
        }
        return -1;
    }
}