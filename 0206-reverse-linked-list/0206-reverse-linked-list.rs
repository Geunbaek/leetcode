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
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut cur_node = None;
        let mut iter = head.as_ref();
        while iter != None {
            if let Some(ref node) = iter {
                let mut new_node = ListNode::new(node.val);

                if cur_node != None {
                    if let Some(cur_box) = cur_node {
                        new_node.next = Some(cur_box);
                    }
                }
                cur_node = Some(Box::new(new_node));
                iter = node.next.as_ref();
            }
        }
        cur_node
    }
}
