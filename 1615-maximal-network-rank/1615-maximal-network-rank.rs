use std::cmp;

impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut connect: Vec<Vec<usize>> = vec![vec![0; n]; n];
        let mut degree: Vec<usize> = vec![0; n];
        let mut answer = 0;
        
        for path in roads.iter() {
            let u = path[0] as usize;
            let v = path[1] as usize;
            
            connect[u][v] = 1;
            connect[v][u] = 1;
            degree[u] += 1;
            degree[v] += 1;
        }
        
        for i in 0..n {
            for j in 0..n {
                if i == j {
                    continue;
                }
                if connect[i][j] == 1 {
                    answer = cmp::max(answer, degree[i] + degree[j] - 1);
                } else {
                    answer = cmp::max(answer, degree[i] + degree[j]);
                }
            }
        }
        answer as i32
    }
}