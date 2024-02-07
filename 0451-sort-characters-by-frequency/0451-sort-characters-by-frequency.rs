use std::collections::HashMap;

impl Solution {
    pub fn frequency_sort(s: String) -> String {
        let mut counter: HashMap<char, i32> = HashMap::new();
        
        for c in s.chars() {
            counter.entry(c).and_modify(|x| *x += 1).or_insert(1);
        }
        
        let mut sc: Vec<char> = s.chars().collect();
        
        sc.sort_by(|a, b| {
            let count_a = counter[a];
            let count_b = counter[b];
            if count_a == count_b {
                return b.cmp(a);
            } else {
                return count_b.cmp(&count_a);
            }
        });
        
        return sc.iter().map(|x| x.to_string()).collect::<Vec<String>>().join("");
    }
}