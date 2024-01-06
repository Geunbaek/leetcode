use std::collections::BinaryHeap;
use std::cmp;

impl Solution {
    pub fn job_scheduling(start_time: Vec<i32>, end_time: Vec<i32>, profit: Vec<i32>) -> i32 {
        let n = start_time.len();
        
        let mut jobs: Vec<(i32, i32, i32)> = vec![];
        let mut h: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        
        for i in 0..n {
            let s = start_time[i];
            let e = end_time[i];
            let p = profit[i];
            
            jobs.push((s, e, p));
        }
        
        jobs.sort();
        let mut max = 0;
        
        for i in 0..n {
            let (s, e, p) = jobs[i];
            
            while !h.is_empty() && s >= -h.peek().unwrap().0 {
                let (end, profit) = h.pop().unwrap();
                max = cmp::max(max, -profit);
            }
            
            h.push((-e, -(p + max)));
        }
        
        let mut ans = 0;
        
        while let Some((e, p)) = h.pop() {
            ans = cmp::max(ans, -p);
        }
        
        ans
        
    }
}