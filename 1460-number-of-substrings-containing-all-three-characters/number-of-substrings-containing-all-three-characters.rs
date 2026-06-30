use std::collections::HashMap;


impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let s_chars: Vec<char> = s.chars().collect();
        let n = s_chars.len();
        
        let mut cache = HashMap::new();
        let mut answer = 0;

        let mut left = 0;
        let mut right = 0;

        while right < n {
            *cache.entry(s_chars[right]).or_insert(0) += 1;

            while cache.len() == 3 {
                answer += (n - right) as i32;

                if let Some(count) = cache.get_mut(&s_chars[left]) {
                    *count -= 1;
                    if *count == 0 {
                        cache.remove(&s_chars[left]);
                    }
                }
                left += 1;
            }
            right += 1;
        }
        answer
    }
}
