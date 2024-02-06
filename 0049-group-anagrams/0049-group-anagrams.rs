use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut cache: HashMap<String, Vec<String>> = HashMap::new();
        let mut ans: Vec<Vec<String>> = vec![];
        
        for s in strs.iter() {
            let mut sorted_vs:Vec<String> = s.chars().map(|x| x.to_string()).collect();
            sorted_vs.sort();
            let vs_string = sorted_vs.join("");
            
            let el = cache.entry(vs_string).or_insert(vec![]);
            el.push(s.clone());
            
        }
        
        for value in cache.values() {
            ans.push(value.clone());
        }
        ans
    }
}