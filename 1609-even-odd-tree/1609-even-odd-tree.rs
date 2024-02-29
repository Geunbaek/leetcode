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
    pub fn is_even_odd_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn dfs(trees: &mut Vec<Vec<i32>>, depth: usize, node: Option<Rc<RefCell<TreeNode>>>) {
            match (node) {
                Some(node) => {
                    let node = node.borrow();
                    trees[depth].push(node.val);
                    dfs(trees, depth + 1, node.left.clone());
                    dfs(trees, depth + 1, node.right.clone());
                },
                None => {}
            }
        }
        
        fn is_increasing(nodes: &Vec<i32>) -> bool {
            let n = nodes.len();
            
            if nodes[0] % 2 == 0 {
                return false;
            }
            
            for i in 1..n {
                if nodes[i] % 2 == 0 {
                    return false;
                }
                if nodes[i] <= nodes[i - 1] {
                    return false;
                }
            }
            true
        }
        
        fn is_decreasing(nodes: &Vec<i32>) -> bool {
            let n = nodes.len();
            
            if nodes[0] % 2 != 0 {
                return false;
            }
            
            for i in 1..n {
                if nodes[i] % 2 != 0 {
                    return false;
                }
                if nodes[i] >= nodes[i - 1] {
                    return false;
                }
            }
            true
        }
         
        let mut trees: Vec<Vec<i32>> = vec![vec![]; 1000001];
        dfs(&mut trees, 0, root);
        
        for i in 0..1000001 {
            println!("{:?}", trees[i]);
            if trees[i].len() == 0 {
                break;
            }
            
            if i % 2 == 0 {
                if (!is_increasing(&trees[i])) {
                    return false;
                }
            } else {
                if (!is_decreasing(&trees[i])) {
                    return false;
                }
            }
        }
        true   
    }
}