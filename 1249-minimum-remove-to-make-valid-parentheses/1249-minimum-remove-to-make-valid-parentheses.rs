impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        let n = s.len();
        
        let s: Vec<char> = s.chars().collect();
        let mut valid = vec![1; n];
        let mut stack: Vec<(char, usize)> = vec![];
        
        for (i, c) in s.iter().enumerate() {
            if *c == '(' {
                stack.push((*c, i));
                continue;
            }
            
            if *c == ')' {
                if stack.is_empty() {
                    valid[i] = 0;
                } else if stack.last().unwrap().0 == '(' {
                    stack.pop();
                } else {
                    valid[i] = 0;
                }
            }
        }
        
        for (c, i) in stack {
            valid[i] = 0;
        }
        
        let mut answer = String::new();
        
        for i in 0..n {
            if valid[i] == 1 {
                answer.push(s[i]);
            }
        }
        answer
    }
}