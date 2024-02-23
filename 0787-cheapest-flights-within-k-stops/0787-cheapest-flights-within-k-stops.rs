use std::{collections::{BinaryHeap}, cmp};

impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        fn dij(graph: &Vec<Vec<(usize, isize)>>, start: usize, end: usize, k: usize) -> i32 {
            let mut h: BinaryHeap<(isize, usize, usize)> = BinaryHeap::new();
            let n = graph.len();
            
            h.push((0, start, 0));
            
            let mut dist: Vec<Vec<isize>> = vec![vec![isize::MAX; k + 2]; n];
            let mut min = isize::MAX;
    
            while let Some((cost, now, count)) = h.pop() {
                let cost = -cost;
                if now == end {
                    min = cmp::min(min, cost);
                    continue
                }
                
                if dist[now][count] <= cost {
                    continue
                }
                dist[now][count] = cost;
                for (next, c) in graph[now].iter() {
                    if count > k {
                        continue;
                    }
                    if cost + *c >= dist[*next][count + 1] {
                        continue;
                    }
                    h.push((-(cost + *c), *next, count + 1));
                }
            }
            if min == isize::MAX {
                return -1;
            }
            return min as i32;
        }
        
        let n = n as usize;
        let mut graph: Vec<Vec<(usize, isize)>> = vec![vec![]; n + 1];
        
        for flight in flights {
            let (start, end, cost) = (flight[0] as usize, flight[1] as usize, flight[2] as isize);
            graph[start].push((end, cost));
        }
        
        return dij(&graph, src as usize, dst as usize, k as usize);
    }
}