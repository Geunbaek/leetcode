use std::collections::VecDeque;

impl Solution {
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let n = graph.len();
        
        let mut degree = vec![0; n];
        let mut rev_graph:Vec<Vec<usize>> = vec![vec![]; n];
        let mut answer = vec![];
        
        for i in 0..n {
            for node in graph[i].iter() {
                degree[i] += 1;
                rev_graph[*node as usize].push(i);
            }
        }
        
        let mut q: VecDeque<usize> = VecDeque::new();
        
        for i in 0..n {
            if degree[i] == 0 {
                q.push_back(i);
            }
        }
        
        while let Some(now) = q.pop_front() {
            answer.push(now as i32);
            for next in rev_graph[now].iter() {
                degree[*next] -= 1;
                if degree[*next] == 0 {
                    q.push_back(*next);
                }
            }
        }
        answer.sort();
        return answer;
    }
}