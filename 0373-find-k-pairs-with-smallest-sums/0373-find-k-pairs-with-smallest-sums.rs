use std::collections::{BinaryHeap, HashSet};

impl Solution {
    pub fn k_smallest_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let n = nums1.len();
        let m = nums2.len();
        let mut k = k;
        
        let mut h: BinaryHeap<(i32, (i32, i32))> = BinaryHeap::new();
        h.push((-(nums1[0] + nums2[0]), (0, 0)));
        
        let mut visited: HashSet<(i32, i32)> = HashSet::new();

        let mut answer: Vec<Vec<i32>> = vec![];
        
        while k > 0 && !h.is_empty() {
            let (sum, (i, j)) = h.pop().unwrap();
            answer.push(vec![nums1[i as usize], nums2[j as usize]]);
            
            if ((i + 1) as usize) < n && !visited.contains(&(i + 1, j)) {
                visited.insert((i + 1, j));
                h.push((-(nums1[(i + 1) as usize] + nums2[j as usize]), (i + 1, j)));
            }
            
            if ((j + 1) as usize) < m && !visited.contains(&(i, j + 1)) {
                visited.insert((i, j + 1));
                h.push((-(nums1[i as usize] + nums2[(j + 1) as usize]), (i , j + 1)));
            }
            k -= 1;
        }
        return answer;
    }
}