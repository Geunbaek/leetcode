use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut cache: HashMap<char, char> = HashMap::new();
        let mut ban: HashSet<char> = HashSet::new();
        
        for (c1, c2) in s.chars().zip(t.chars()) {
            if cache.contains_key(&c1) {
                if cache[&c1] != c2 {
                    return false; 
                }

            } else {
                if ban.contains(&c2) {
                    return false;
                }
                cache.insert(c1, c2);
                ban.insert(c2);
            }
        }
        true
    }
}