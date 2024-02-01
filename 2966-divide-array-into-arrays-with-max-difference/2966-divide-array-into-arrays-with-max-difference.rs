impl Solution {
    pub fn divide_array(nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort();
        
        let mut answer: Vec<Vec<i32>> = vec![vec![]];
        
        for num in sorted_nums.iter() {
            let n = answer.len();
            
            if answer[n - 1].len() < 3 {
                answer[n - 1].push(*num);
            } else {
                if answer[n - 1][2] - answer[n - 1][0] > k {
                    return vec![];
                }
                answer.push(vec![*num]);
            }
        }
        let n = answer.len();
        if answer[n - 1][2] - answer[n - 1][0] > k {
            return vec![];
        }
        return answer;     
    }
}