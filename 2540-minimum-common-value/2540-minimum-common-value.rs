use std::collections::HashSet;
use std::iter::FromIterator;
impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let nums1: HashSet<i32> = nums1.into_iter().collect();
        let nums2: HashSet<i32> = nums2.into_iter().collect();
        let mut inter = nums1.intersection(&nums2);
        let mut sorted_inter: Vec<&i32> = inter.into_iter().collect();
        sorted_inter.sort();
        
        if sorted_inter.is_empty() {
            return -1;
        }
        *sorted_inter[0]
    }
}