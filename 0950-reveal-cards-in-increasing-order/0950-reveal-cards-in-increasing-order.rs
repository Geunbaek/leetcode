use std::collections::VecDeque;

impl Solution {
    pub fn deck_revealed_increasing(deck: Vec<i32>) -> Vec<i32> {
        let mut deck = deck;
        deck.sort();
        
        let mut deck = VecDeque::from(deck);
        let n = deck.len();
        let mut q = VecDeque::from((0..n).map(|x| x).collect::<Vec<usize>>());
        
        let mut answer = vec![0; n];
        
        while let Some(i) = q.pop_front() {
            answer[i] = deck.pop_front().unwrap();
            if let Some(i) = q.pop_front() {
                q.push_back(i);
            }
        }
        answer
    }
}