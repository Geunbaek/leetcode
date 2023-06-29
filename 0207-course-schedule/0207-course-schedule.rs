use std::collections::{HashSet, VecDeque};

impl Solution {    
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let n = num_courses as usize;
        
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        let mut degree: Vec<usize> = vec![0;n];
        
        for pre in prerequisites.iter() {
            let u = pre[0] as usize;
            let v = pre[1] as usize;
            if u == v { return false; }
            graph[u].push(v);
            degree[v] += 1;
        }
        
        let mut visited: HashSet<usize> = HashSet::new();
        let mut q: VecDeque<usize> = VecDeque::new();
        
        for i in 0..n {
            if degree[i] != 0 { continue; }
            q.push_back(i);
            visited.insert(i);
        }
        
        while let Some(now) = q.pop_front() {
            for next in &graph[now]{
                if visited.contains(next) {
                    return false;
                }
                
                degree[*next] -= 1;
                if degree[*next] != 0 {
                    continue;
                }
                
                visited.insert(*next);
                q.push_back(*next);
            }
        }

        return visited.len() == n;
    }
}