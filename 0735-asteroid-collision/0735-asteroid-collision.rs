impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut stack:Vec<i32> = vec![];
        
        for asteroid in asteroids.iter() {
            stack.push(*asteroid);
            let mut n = stack.len();
            
            while n >= 2 {
                if (stack[n - 1] < 0 && stack[n - 2] > 0) {
                    let l1 = stack.pop().unwrap();
                    let l2 = stack.pop().unwrap();
                    if l1.abs() > l2.abs() {
                        stack.push(l1);
                    } else if l1.abs() < l2.abs() {
                        stack.push(l2);
                    } 
                } else {
                    break;
                }
                n = stack.len();
            }
        }
        return stack;
    }
}