use std::collections::VecDeque;

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        fn bfs(n: usize, graph: &Vec<Vec<(usize, isize)>>, start: usize) -> Vec<i32> {
            let mut q: VecDeque<(usize, isize)> = VecDeque::new();
            q.push_back((0, 0));
            q.push_back((start, 0));
            
            let mut visited: Vec<isize> = vec![isize::MAX; n + 1];
            visited[0] = 0;
            visited[start] = 0;
            
            while let Some((now, current_time)) = q.pop_front() {
                for (next, start_time) in graph[now].iter() {
                    if visited[*next] <= *start_time {
                        continue;
                    }
                    
                    if current_time > *start_time {
                        continue;
                    }
                    
                    visited[*next] = *start_time;
                    q.push_back((*next, *start_time));
                }
            }
            
            let mut answer: Vec<i32> = vec![];
            
            for i in 0..n {
                if visited[i] != isize::MAX {
                    answer.push(i as i32);
                }
            }
            answer
        }
        
        let n = n as usize;
        let mut graph: Vec<Vec<(usize, isize)>> = vec![vec![]; n];
        
        graph[0].push((first_person as usize, 0));
        for meeting in meetings {
            let x = meeting[0] as usize;
            let y = meeting[1] as usize;
            let time = meeting[2] as isize;
            graph[x].push((y, time));
            graph[y].push((x, time));
        }
        
        bfs(n, &graph, first_person as usize)
    }
}