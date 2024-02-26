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
impl Solution {
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if let (Some(p), Some(q)) = (p.clone(), q.clone()) {
            let p = p.borrow();
            let q = q.borrow();
            
            if p.val != q.val {
                return false;
            }
            
            let mut ret = true;
 
            if p.left == None && q.left != None {
                return false;
            } else if q.left == None && p.left != None {
                return false;
            } else {
                ret &= Solution::is_same_tree(p.left.clone(), q.left.clone());
            }
            
            if p.right == None && q.right != None {
                return false;
            } else if q.right == None && p.right != None {
                return false;
            } else {
                ret &= Solution::is_same_tree(p.right.clone(), q.right.clone());
            } 
            return ret;
        
        } else {
            if p == None && q == None {
                return true;
            }
            return false;
        }
    }
}