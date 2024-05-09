use std::collections::BinaryHeap;
impl Solution {
    pub fn maximum_happiness_sum(happiness: Vec<i32>, k: i32) -> i64 {
        let mut h = BinaryHeap::from(happiness);
        let mut answer = 0;
        for i in 0..k {
            if let Some(max) = h.pop() {
                if max >= i {
                    answer += (max - i) as i64;
                }
            }
        }
        answer
    }
}