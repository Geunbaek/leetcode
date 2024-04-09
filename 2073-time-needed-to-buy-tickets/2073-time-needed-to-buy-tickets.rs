impl Solution {
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {
        let mut answer = 0;
        let mut tickets = tickets;
        
        let n = tickets.len();
        
        loop {
            for i in 0..n {
                if tickets[i] == 0 {
                    continue;
                }
                
                tickets[i] -= 1;
                answer += 1;
                
                if tickets[i] == 0 && k == i as i32 {
                    return answer;
                }
            }
        }
        answer + tickets[k as usize]
    }
}