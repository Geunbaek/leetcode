impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut stack: Vec<usize> = vec![];
        let mut a_stack: Vec<usize> = vec![];
        
        for (i, c) in s.chars().enumerate() { 
            if c == '(' {
                stack.push(i);
                continue;
            }
            
            if c == '*' {
                a_stack.push(i);
                continue;
            }
            
            if c == ')' {
                if !stack.is_empty() {
                    stack.pop();
                } else if !a_stack.is_empty() {
                    a_stack.pop();
                } else {
                    return false;
                }
            }
        }
        
        while !stack.is_empty() && !a_stack.is_empty() {
            if stack.pop().unwrap() > a_stack.pop().unwrap() {
                return false;
            }
        }
        return stack.is_empty();
    }
}