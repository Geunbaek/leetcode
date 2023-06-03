use std::{collections::VecDeque, cmp};

impl Solution {
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        
        for (i, num) in manager.into_iter().enumerate() {
            if num == -1 {
                continue;
            }
            graph[num as usize].push(i as usize);
        }
        
        let mut q: VecDeque<(usize, i32)> = VecDeque::new();
        q.push_back((head_id as usize , inform_time[head_id as usize]));
        
        let mut answer = 0;
        
        while let Some((now, time)) = q.pop_front() {
            answer = cmp::max(answer, time);
            
            for next in graph[now as usize].iter() {
                q.push_back((*next, time + inform_time[*next]));
            }
        }
        return answer;
    }
}