use std::collections::HashMap;
impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut result: HashMap<i32, i32> = HashMap::new();

        for m in &matches {
            let winner = m[0];
            let loser = m[1];
            let w_cnt = result.entry(winner).or_insert(0);
            let l_cnt = result.entry(loser).or_insert(0);
            *l_cnt += 1;
        }

        let mut answer = vec![vec![], vec![]];
        
        for (player, count) in result {
            match count {
                0 => answer[0].push(player),
                1 => answer[1].push(player),
                _ => continue,
            }
        }
        
        for i in 0..=1 {
            answer[i].sort();
        }

        return answer;
        
    }
}