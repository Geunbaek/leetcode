use std::collections::HashSet;

impl Solution {
    pub fn find(p: &mut Vec<usize>, node: usize) -> usize {
        if node != p[node] {
            p[node] = Solution::find(p, p[node]);
        }
        return p[node];
    }
    
    pub fn union(p: &mut Vec<usize>, node1: usize, node2: usize) {
        let node1_parent = Solution::find(p, node1);
        let node2_parent = Solution::find(p, node2);
        p[node1_parent] = node2_parent;
    }
    
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let N: usize = is_connected.len();
        let mut p: Vec<usize> = (0..N).map(|i| i).collect();
        for y in 0..N {
            for x in y+1..N {
                if is_connected[y][x] == 0 {
                    continue;
                }
                Solution::union(&mut p, y, x);
            }
        }
        
        let mut answer: HashSet<usize> = HashSet::new();
        
        for num in 0..N {
            answer.insert(Solution::find(&mut p, num));
        }
        
        return answer.len() as i32;
    }
}