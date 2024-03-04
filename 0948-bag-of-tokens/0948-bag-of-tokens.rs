use std::cmp;
impl Solution {
    pub fn bag_of_tokens_score(tokens: Vec<i32>, power: i32) -> i32 {
        if tokens.len() == 0 {
            return 0;
        }
        
        let mut tokens = tokens;
        let mut power = power;
        tokens.sort();
        
        let (mut left, mut right) = (0_usize, tokens.len() - 1);
        let mut score = 0;
        let mut max = 0;
        while left <= right {
            if power >= tokens[left] {
                power -= tokens[left];
                left += 1;
                score += 1;
            } else {
                if score >= 1 {
                    power += tokens[right];
                    right -= 1;
                    score -= 1;
                } else {
                    break;
                }
            }
            max = cmp::max(max, score);
        }
        max
    }
}