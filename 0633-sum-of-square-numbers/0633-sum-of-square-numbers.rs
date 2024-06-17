impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {
        if c == 0 {
            return true;
        }
        let max = ((c as f64).sqrt() as i32) + 1;
        
        for a in 1..max {
            let b2 = c as f64 - (a * a) as f64;
            let sqrt_b = b2.sqrt() as i32;
            if (sqrt_b * sqrt_b) as f64 == b2 {
                return true;
            } 
        }
        
        false
    }
}