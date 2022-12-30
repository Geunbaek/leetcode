impl Solution {
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = graph.len();
        let mut answer: Vec<Vec<i32>> = vec![];
        let mut visited = vec![0;n];
        
        fn dfs(graph:&Vec<Vec<i32>>,  node:i32, path:Vec<i32>, n: i32, answer: &mut Vec<Vec<i32>>, visited:&mut Vec<i32> ) {
            if node == n as i32 - 1 {
                answer.push(path);
                return;
            }
            for _next in &graph[node as usize] {
                if visited[*_next as usize] == 0 {
                    visited[*_next as usize] = 1;
                    let mut newPath = path.clone();
                    newPath.push(*_next); 
                    dfs(graph, *_next, newPath, n, answer, visited);
                    visited[*_next as usize] = 0;
                }
            }
        };
        dfs(&graph, 0, vec![0], n as i32, &mut answer, &mut visited);
        answer
    }
}