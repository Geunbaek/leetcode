use std::{collections::BinaryHeap, cmp};

impl Solution {
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let mut nums:Vec<(i64, i64)> = vec![];
        let mut heap: BinaryHeap<_> = BinaryHeap::new();
        
        let n = nums1.len();
        let k: usize = k as usize;
        
        for i in 0..n {
            let (n1, n2) = (nums1[i], nums2[i]);
            nums.push((n1 as i64, n2 as i64));
        }
        
        nums.sort_by(|a, b| b.1.cmp(&a.1));
        let mut sum: i64 = 0;
        
        for i in 0..k {
            let (n1, n2) = nums[i];
            heap.push(-n1);
            sum += n1;
        }
        
        let mut answer: i64 = (sum * nums[k - 1].1) as i64;
  
        for i in k..n {
            let (n1, n2) = nums[i];
            let smallest = heap.pop().unwrap();
            sum += smallest;
            sum += n1;
            heap.push(-n1);
            answer = cmp::max(answer, (sum * n2) as i64);
        }
        
        return answer
    }
}