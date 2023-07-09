impl Solution {
    pub fn largest_variance(s: String) -> i32 {
        let mut counter:Vec<usize> = vec![0; 26];
        
        for c in s.chars() {
            counter[c as usize - 'a' as usize] += 1;
        }
        
        let mut answer = 0;
        
        for i in 0..26 {
            for j in 0..26 {
                if (i == j || counter[i] == 0 || counter[j] == 0) {
                    continue;
                }
                
                let major: usize = 'a' as usize + i;
                let minor: usize = 'a' as usize + j;
                let mut major_count = 0;
                let mut minor_count = 0;
                
                let mut rest_minor = counter[j];
                
                for c in s.chars() {
                    if c as usize == major {
                        major_count += 1;
                    }
                    if c as usize == minor {
                        minor_count += 1;
                        rest_minor -= 1;
                    }
                    if minor_count > 0 {
                        answer = std::cmp::max(answer, major_count - minor_count);
                    }
                    if major_count < minor_count && rest_minor > 0 {
                        major_count = 0;
                        minor_count = 0;
                    }
                }
            }
        }
        return answer;
    }
}