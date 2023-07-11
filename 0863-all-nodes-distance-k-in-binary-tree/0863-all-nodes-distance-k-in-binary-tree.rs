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
use std::collections::{VecDeque, HashSet};

impl Solution {
    pub fn make_graph(graph: &mut Vec<Vec<i32>>, node: Option<Rc<RefCell<TreeNode>>>) {
        if let Some(n) = node {
            let n = n.borrow();
            let val = n.val;
            
            if let Some(left) = n.left.clone() {
                let left = left.borrow();
                let left_val = left.val;
                graph[val as usize].push(left_val);
                graph[left_val as usize].push(val);
                Solution::make_graph(graph, n.left.clone());
            }
            
            if let Some(right) = n.right.clone() {
                let right = right.borrow();
                let right_val = right.val;
                graph[val as usize].push(right_val);
                graph[right_val as usize].push(val);
                Solution::make_graph(graph, n.right.clone());
            }

        } 
    }
    
    pub fn bfs(graph: &Vec<Vec<i32>>, target: Option<Rc<RefCell<TreeNode>>>, k: i32) -> Vec<i32> {
        let mut q: VecDeque<(i32, i32)> = VecDeque::new();
        let mut answer: Vec<i32> = vec![];
        let mut visited: HashSet<i32> = HashSet::new();

        if let Some(t) = target {
            let t = t.borrow();
            let t_val = t.val;
            q.push_back((t_val, 0));
            visited.insert(t_val);
        } else {
            return answer;
        }
     
        
        while let Some((node, cnt)) = q.pop_front() {
            if cnt == k {
                answer.push(node);
            }
            
            if cnt > k {
                continue;
            }
            
            for next in graph[node as usize].iter() {
                if visited.contains(next) {
                    continue;
                }
                visited.insert(*next);
                q.push_back((*next, cnt + 1));
            }
        }
        return answer;
    }
    
    
    pub fn distance_k(root: Option<Rc<RefCell<TreeNode>>>, target: Option<Rc<RefCell<TreeNode>>>, k: i32) -> Vec<i32> {
        let mut graph:Vec<Vec<i32>> = vec![vec![]; 501];
        Solution::make_graph(&mut graph, root);
        
        return Solution::bfs(&graph, target, k);
    }
}