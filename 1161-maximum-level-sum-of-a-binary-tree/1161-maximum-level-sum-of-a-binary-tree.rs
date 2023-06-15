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
    pub fn dfs(tree_info: &mut Vec<i32>, node: Option<Rc<RefCell<TreeNode>>>, depth: usize, visited: &mut Vec<bool>) {
        match node {
            Some(node) => {
                let node_ref = node.borrow();
                visited[depth] = true;
                tree_info[depth] += node_ref.val;
                
                Solution::dfs(tree_info, node_ref.left.clone(), depth + 1, visited);      
                Solution::dfs(tree_info, node_ref.right.clone(), depth + 1, visited);
            }
            None => {
                return;
            }
        }
    }
    
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut tree_info: Vec<i32> = vec![0;10001];
        let mut visited: Vec<bool> = vec![false;10001];
        
        Solution::dfs(&mut tree_info, root, 1, &mut visited);
        
        let mut max = -i32::MAX;
        let mut answer: i32 = 0;
        for i in 1..=10000 {
            if visited[i] == false {
                break;
            }
            if max >= tree_info[i] {
                continue;
            }
            max = tree_info[i];
            answer = i as i32;
        }
        return answer;
    }
}