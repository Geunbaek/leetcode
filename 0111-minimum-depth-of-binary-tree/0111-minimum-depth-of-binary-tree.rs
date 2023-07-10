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


//   pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
//         fn dfs(n: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
//             if let Some(node) = n {
//                 let node = node.borrow();

//                 if node.left.is_none() && node.right.is_none() { return 1 }

//                 let mut res = i32::MAX;

//                 if node.left.is_some() { res = res.min(dfs(&node.left) + 1) }
//                 if node.right.is_some() { res = res.min(dfs(&node.right) + 1) }

//                 return res;
//             }

//             0
//         }

//         dfs(&root)
use std::cmp;
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn dfs(node: Option<Rc<RefCell<TreeNode>>>, depth: i32) -> i32 {
        if let Some(n) = node {
            let n = n.borrow();
            
            if n.left.is_none() && n.right.is_none() {
                return depth;
            }
            
            let mut ret = i32::MAX;
            if n.left.is_some() { ret = ret.min(Solution::dfs(n.left.clone(), depth + 1)) }
            if n.right.is_some() { ret = ret.min(Solution::dfs(n.right.clone(), depth + 1)) }
            return ret;
        } 
        return 0;
    }
    
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        return Solution::dfs(root,1);
    }
}