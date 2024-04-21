use std::collections::VecDeque;

impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        let n = n as usize;
        let source = source as usize;
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        
        for edge in edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            
            graph[u].push(v);
            graph[v].push(u);
        }
        
        let mut q: VecDeque<usize> = VecDeque::from([source as usize]);
        let mut visited: Vec<bool> = (0..n).map(|x| {
            if x == source {
                true
            } else {
                false
            }
        }).collect();
        
        while let Some(now) = q.pop_front() {
            if now == destination as usize {
                return true;
            }
            
            for next in graph[now].iter() {
                if visited[*next] {
                    continue;
                }
                
                visited[*next] = true;
                q.push_back(*next);
            }
        }
        false
    }
}