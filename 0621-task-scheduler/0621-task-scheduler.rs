use std::collections::{BinaryHeap, HashMap};


impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut freq = vec![0; 26];
        
        for task in tasks.iter() {
            let index = ((*task as u8) - ('A' as u8)) as usize;
            freq[index] += 1;
        }
        
        freq.sort();
        
        let max_freq = freq[25] - 1;
        let mut idle = max_freq * n;
        
        for i in (0..25).rev() {
            idle -= std::cmp::min(max_freq, freq[i]);
        }
        
        if idle > 0 {
            return idle + tasks.len() as i32;
        }
        tasks.len() as i32
    }
}