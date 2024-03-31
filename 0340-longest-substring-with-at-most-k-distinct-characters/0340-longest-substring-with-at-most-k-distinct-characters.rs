use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring_k_distinct(s: String, k: i32) -> i32 {
        let n = s.len();
        let k = k as usize;
        let mut cache: HashMap<char, i32> = HashMap::new();
        
        let mut chars_vec: Vec<char> = s.chars().collect();
        
        let mut left = 0_usize;
        let mut answer = 0;
        
        for right in 0..n {
            cache.entry(chars_vec[right]).and_modify(|x| *x += 1).or_insert(1);
            
            while left < right && cache.len() > k {
                cache.entry(chars_vec[left]).and_modify(|x| *x -= 1);
                if cache[&chars_vec[left]] == 0 {
                    cache.remove(&chars_vec[left]);
                }
                left += 1;
            }  
            if cache.len() <= k {
                answer = std::cmp::max(answer, right - left + 1);
            }
        }
        answer as i32
    }
}