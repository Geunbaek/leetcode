use std::collections::BinaryHeap;

impl Solution {
    pub fn max_profit_assignment(difficulty: Vec<i32>, profit: Vec<i32>, worker: Vec<i32>) -> i32 {
        let mut jobs: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        let mut h: BinaryHeap<i32> = BinaryHeap::new();
        let mut answer = 0;
        for (d, p) in difficulty.iter().zip(&profit) {
            jobs.push((-d, *p));
        }
        
        let mut worker = worker.clone();
        worker.sort();
        for ability in worker {
            while !jobs.is_empty() && -jobs.peek().unwrap().0 <= ability {
                let (d, p) = jobs.pop().unwrap();
                h.push(p);
            }
            
            if !h.is_empty() {
                answer += h.peek().unwrap();
            }
        }
        answer
    }
}