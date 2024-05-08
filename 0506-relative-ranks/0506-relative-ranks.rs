impl Solution {
    pub fn find_relative_ranks(score: Vec<i32>) -> Vec<String> {
        let n = score.len();
        
        let mut answer: Vec<String> = vec![String::new(); n];
        
        let mut score: Vec<(usize, i32)> = score.iter().enumerate().map(|(i, x)| (i, *x)).collect();
        
        score.sort_by(|a, b| b.1.cmp(&a.1));
        
        for (i, (j, s)) in score.iter().enumerate() {
            if i == 0 {
                answer[*j] = String::from("Gold Medal");
            } else if i == 1 {
                answer[*j] = String::from("Silver Medal");
            } else if i == 2 {
                answer[*j] = String::from("Bronze Medal");
            } else {
                answer[*j] = (i + 1).to_string();   
            }
        }
        
        return answer;
    }
}