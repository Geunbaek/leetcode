use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, k: i32) -> i32 {
        let mut h: BinaryHeap<(isize, i32)> = BinaryHeap::new();
        let mut counter: HashMap<i32, isize> = HashMap::new();
        
        for num in arr {
            counter.entry(num).and_modify(|x| *x += 1).or_insert(1);
        }
        
        for (key, value) in counter {
            h.push((-value, key));
        }
        
        for _ in 0..k {
            if let Some((count, key)) = h.pop() {
                if -count > 1 {
                    h.push((count + 1, key));
                } else {
                    continue;
                }
            } else {
                break;
            }
        }
        h.len() as i32
    }
}