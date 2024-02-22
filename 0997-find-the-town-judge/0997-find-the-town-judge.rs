use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        if n == 1 {
            return 1;
        }
        let mut counter: HashMap<i32, i32> = HashMap::new();
        let mut ban: HashSet<i32> = HashSet::new();
        let mut last = 0;
        for t in trust {
            let a = t[0];
            let b = t[1];
            counter.entry(b).and_modify(|x| *x += 1).or_insert(1);
            last = b;
            ban.insert(a);
        }
        
        for (b, count) in counter {
            if count == n - 1 && !ban.contains(&b) {
                return b;
            }
        }
        return -1;
    }
}