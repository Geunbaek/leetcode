use std::{collections::BinaryHeap, cmp};

impl Solution {
    pub fn mincost_to_hire_workers(quality: Vec<i32>, wage: Vec<i32>, k: i32) -> f64 {
        let n = quality.len();
        let k = k as usize;
        
        let mut cost = f64::MAX;
        let mut qual = 0;
        let mut ratios = vec![];
        
        for i in 0..n {
            let w = wage[i] as f64;
            let q = quality[i] as f64;
            
            ratios.push((w / q, q as i32));
        }
        
        ratios.sort_by(|a, b| a.partial_cmp(b).unwrap());
        
        let mut workers: BinaryHeap<i32> = BinaryHeap::new();
        
        for i in 0..n {
            workers.push(ratios[i].1);
            qual += ratios[i].1;
            
            if workers.len() > k {
                qual -= workers.pop().unwrap();
            }
            
            if workers.len() == k {
                cost = cost.min(qual as f64 * ratios[i].0);
            }
        }
        cost
    }
}


  
