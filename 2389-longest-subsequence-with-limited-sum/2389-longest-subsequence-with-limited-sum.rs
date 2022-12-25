impl Solution {
    pub fn answer_queries(mut nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        nums.sort();
        let mut answer: Vec<i32> = vec![];
        
        for q in &queries {
            let mut count = 0;
            let mut total = *q;
            
            for num in &nums {
                if total >= *num {
                    total -= *num;
                    count += 1;
                }
            }
            answer.push(count);
        }
        return answer;
    }
}