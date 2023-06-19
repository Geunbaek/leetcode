use std::cmp;

impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut height = 0;
        let mut answer = height;
        
        for diff in &gain {
            height += *diff;
            answer = cmp::max(answer, height);
        }
        answer
    }
}