use std::collections::{VecDeque, HashSet};

impl Solution {
    pub fn shortest_path_length(graph: Vec<Vec<i32>>) -> i32 {
        let n = graph.len();
        
        let mut q: VecDeque<(i32, i32)> = VecDeque::new();
        let mut visited: HashSet<(i32, i32)> = HashSet::new();
        for i in 0..n {
            q.push_back((i as i32, 1 << i as i32));
            visited.insert((i as i32, 1 << i as i32));
        }
        let mut answer = 0;
        
        while !q.is_empty() {
            for _ in 0..q.len() {
                if let Some((u, t)) = q.pop_front() {
                    if t == (1 << n) - 1 {
                        return answer;
                    }
                    for v in graph[u as usize].iter() {
                        if visited.contains(&(*v, t | 1 << *v)) {
                            continue;
                        }
                        q.push_back((*v, t | 1 << *v));                    
                        visited.insert((*v, t | 1 << *v));
                    }
                }
            }
            answer += 1;
        }
        0
    }
}

