use std::collections::{BinaryHeap,HashMap };

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>, limit: i32) -> i32 {
        let n = nums.len();
        let mut limit = limit;
        
        let mut cache: HashMap<i32, i32> = HashMap::new();
        let mut max_h: BinaryHeap<_> = BinaryHeap::new();
        let mut min_h: BinaryHeap<_> = BinaryHeap::new();
        
        let mut answer = 0;
        let mut right = 0;
        
        for left in 0..n {
            while right < n {
                cache.entry(nums[right]).and_modify(|x| *x += 1).or_insert(1);
                max_h.push(nums[right]);
                min_h.push(-nums[right]);
                right += 1;
                
                loop {
                    if let Some(max) = max_h.peek() {
                        match cache.get(&max) {
                            Some(count) => {
                                break;
                            },
                            None => {
                                max_h.pop();
                            }
                        }
                    } else {
                        break;
                    }
                }
                
                loop {
                    if let Some(min) = min_h.peek() {
                        match cache.get(&-min) {
                            Some(count) => {
                                break;
                            },
                            None => {
                                min_h.pop();
                            }
                        }
                    } else {
                        break;
                    }
                }
                
                let max = max_h.peek();
                let min = min_h.peek();
                
                match max {
                    Some(num) => {},
                    None => {break;}
                }
                
                match min {
                    Some(num) => {},
                    None => {break;}
                }
                
             
                if max.unwrap() - -min.unwrap() <= limit {
                    answer = std::cmp::max(answer, right - left);
                } else {
                    break;
                }
            }     
            cache.entry(nums[left]).and_modify(|x| *x -= 1);
            if cache[&nums[left]] == 0 {
                cache.remove(&nums[left]);
            }
        }
        answer as i32
    }
}