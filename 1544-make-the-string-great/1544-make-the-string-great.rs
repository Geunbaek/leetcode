impl Solution {
    pub fn is_lower(c: &char) -> bool {
        return 97 <= *c as u8 && *c as u8 <= 97 + 26;
    }
    
    pub fn is_upper(c: &char) -> bool {
        return 65 <= *c as u8 && *c as u8 <= 65 + 26;
    }
    
    pub fn make_good(s: String) -> String {
        let mut stack: Vec<char> = vec![];
        
        for c in s.chars() {
            if stack.is_empty() {
                stack.push(c);
                continue;
            }
            
            let n = stack.len() - 1;
            let last = stack[n];
            if Solution::is_lower(&last) {
                let last_diff = last as u8 - 'a' as u8;
                if Solution::is_upper(&c) {
                    let c_diff = c as u8 - 'A' as u8;
                    if last_diff == c_diff {
                        stack.pop();
                        continue;
                    }
                }
            } else {
                let last_diff = last as u8 - 'A' as u8;
                if Solution::is_lower(&c) {
                    let c_diff = c as u8 - 'a' as u8;
                    if last_diff == c_diff {
                        stack.pop();
                        continue;
                    }
                }
            }
            stack.push(c);
        }
        let answer: Vec<String> = stack.iter().map(|x| x.to_string()).collect();
        answer.join("")
    }
}