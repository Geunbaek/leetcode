use std::collections::{ HashMap };

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        fn check(t_count: &HashMap<char, usize>, now: &HashMap<char, usize>) -> bool {
            for (key, val) in t_count.iter() {
                if !now.contains_key(key) {
                    return false;
                }
                if now[key] < *val {
                    return false;
                }
            }
            true
        }
        
        let mut t_count: HashMap<char, usize> = HashMap::new();
        let mut now: HashMap<char, usize> = HashMap::new();
        let mut min = s.len();
        let mut ans: Vec<char> = vec![];
        
        for c in t.chars() {
            t_count.entry(c).and_modify(|cnt| *cnt += 1).or_insert(1);
        }
        
        let mut left = 0;
        for (right, c) in s.chars().enumerate() {
            now.entry(c).and_modify(|cnt| *cnt += 1).or_insert(1);
            while check(&t_count, &now) {
                if min > right - left {
                    min = right - left;
                    ans = s[left..right + 1].chars().collect::<Vec<char>>();
                }
                let left_char = s[left..left + 1].chars().collect::<Vec<char>>();
                now.entry(left_char[0]).and_modify(|cnt| *cnt -= 1).or_insert(1);
                left += 1;
            }
        }
        ans.into_iter().collect::<String>()
    }
}


        
        
        