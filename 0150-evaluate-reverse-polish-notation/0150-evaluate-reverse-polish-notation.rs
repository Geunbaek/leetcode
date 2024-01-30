impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<String> = vec![];
        
        for token in tokens.iter() {
            match token.as_str() {
                "-" => {
                    let l1: i32 = stack.pop().unwrap().parse().unwrap();
                    let l2: i32 = stack.pop().unwrap().parse().unwrap();
                    let sub = (l2 - l1).to_string();
                    stack.push(sub);
                },
                "+" => {
                    let l1: i32 = stack.pop().unwrap().parse().unwrap();
                    let l2: i32 = stack.pop().unwrap().parse().unwrap();
                    let add = (l2 + l1).to_string();
                    stack.push(add);
                },
                "*" => {
                    let l1: i32 = stack.pop().unwrap().parse().unwrap();
                    let l2: i32 = stack.pop().unwrap().parse().unwrap();
                    let mul = (l2 * l1).to_string();
                    stack.push(mul);
                },
                "/" => {
                    let l1: i32 = stack.pop().unwrap().parse().unwrap();
                    let l2: i32 = stack.pop().unwrap().parse().unwrap();
                    let div = (l2 / l1).to_string();
                    stack.push(div);
                },
                _ => {
                    stack.push(token.to_string());
                }
            }
        }
        stack.pop().unwrap().parse::<i32>().unwrap()
    }
}