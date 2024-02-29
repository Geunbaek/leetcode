// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn is_even_odd_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut q = VecDeque::new();
        q.extend([root, None]);
        let mut even = false;
        let mut extreme = i32::MIN;
        while !q.is_empty() {
            let node = q.pop_front().unwrap();
            if let Some(n) = node {
                let n = n.borrow();
                let val = n.val;
                if (val % 2 == 0) != even {
                    return false;
                }
                if even {
                    if val < extreme {
                        extreme = val;
                    } else {
                        return false;
                    }
                } else {
                    if val > extreme {
                        extreme = val;
                    } else {
                        return false;
                    }
                }
                if n.left.is_some() {
                    q.push_back(n.left.clone());
                }
                if n.right.is_some() {
                    q.push_back(n.right.clone());
                }
            } else {
                // special case: None switches oddity
                even = !even;
                extreme = if even { i32::MAX } else { i32::MIN };
                if !q.is_empty() {
                    q.push_back(None);
                }
            }
        }
        true
    }
}