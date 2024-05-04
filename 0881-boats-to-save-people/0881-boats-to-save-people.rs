use std::collections::BinaryHeap;

impl Solution {
    pub fn num_rescue_boats(people: Vec<i32>, limit: i32) -> i32 {
        let mut people = people.clone();
        
        people.sort_by(|a, b| b.cmp(&a));
    
        let mut h: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        let mut over = 0;
        
        for weight in people {
            if let Some((min, cnt)) = h.pop() {                
                let min = -min;
                
                if min + weight <= limit {
                    over += 1;
                } else {
                    h.push((-min, cnt));
                    h.push((-weight, 1));
                }
            } else {
                h.push((-weight, 1));
            }
        }
        over + h.len() as i32
    }
}