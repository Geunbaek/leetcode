// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut nums:Vec<i32> = vec![];
        
        let mut node = &head;
        while let Some(now) = node {
            nums.push(now.val);
            node = &now.next;
        }
        
        let n = nums.len();
        
        if n <= 1 {
            return true;
        }
        
        let mid = n / 2 - 1;
        
        for i in 0..=mid {
            if nums[i] != nums[n - i - 1] {
                return false;
            }
        }
        true
    }
}