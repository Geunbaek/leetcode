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
use std::cmp;
use std::collections::HashMap;
impl Solution {
    pub fn find_bottom_left_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn recur(node: Option<Rc<RefCell<TreeNode>>>, index: i32, depth: i32, left_values:&mut HashMap<i32, Vec<(i32, i32)>>, max_depth: &mut i32) {
            *max_depth = cmp::max(*max_depth, depth);
            
            match(node) {
                Some(node) => {
                    let node = node.borrow();
                    
                    left_values.entry(depth).and_modify(|x| x.push((index, node.val))).or_insert(vec![(index, node.val)]);
                    
                    if let Some(left) = node.left.clone() {
                        recur(node.left.clone(), index * 2, depth + 1,  left_values, max_depth);
                    } else {}
                    
                    if let Some(right) = node.right.clone() {
                        recur(node.right.clone(), index * 2 + 1, depth + 1,  left_values, max_depth);
                    } else {}
                },
                None => {}
            }
        }
        
        let mut left_values: HashMap<i32, Vec<(i32, i32)>> = HashMap::new();
        let mut max_depth = 0;
        recur(root, 1, 0, &mut left_values, &mut max_depth);
        let mut lv = left_values[&max_depth].clone();
        lv.sort();
        
        let (_, answer) = lv[0];
        return answer;
    }
}