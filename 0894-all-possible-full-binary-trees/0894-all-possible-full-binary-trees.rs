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
    pub fn all_possible_fbt(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        if n % 2 == 0 {
            return vec![];
        } 
        
        if n == 1 {
            return vec![Some(Rc::new(RefCell::new(TreeNode::new(0))))];
        }
        
        let mut answer:Vec<Option<Rc<RefCell<TreeNode>>>> = vec![];
        let mut i = 1;
        
        loop {
            if i >= n {
                break;
            }
            let left = Solution::all_possible_fbt(i);
            let right = Solution::all_possible_fbt(n - i - 1);
            
            for l in &left {
                for r in &right {
                    let mut root = Rc::new(RefCell::new(TreeNode {
                        val: 0,
                        left: l.clone(),
                        right: r.clone(),
                    }));
                    answer.push(Some(root));
                }
            }
            i += 2;
        }
        return answer;
    }
}

