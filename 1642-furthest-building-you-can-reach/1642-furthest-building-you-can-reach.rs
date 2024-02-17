use std::collections::BinaryHeap;

impl Solution {
    pub fn furthest_building(heights: Vec<i32>, bricks: i32, ladders: i32) -> i32 {   
        let n = heights.len();
        let mut bricks = bricks;
        let mut heap: BinaryHeap<i32> = BinaryHeap::new();
        
        for i in 1..n {
            let diff = heights[i] - heights[i - 1];
            
            if diff <= 0 {
                continue;
            }
            
            heap.push(-diff);
            
            if heap.len() <= ladders as usize {
                continue;
            }
            
            let min_diff = -heap.pop().unwrap();
            bricks -= min_diff;
            
            if bricks < 0 {
                return i as i32 - 1;
            }
        }
        return n as i32 - 1;
    }
}