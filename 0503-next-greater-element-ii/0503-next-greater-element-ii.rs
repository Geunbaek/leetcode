impl Solution {
    pub fn next_greater_elements(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut stack: Vec<(usize, i32)> = vec![];
        let mut answer = vec![-1; n];
        
        for i in 0..nums.len() * 2 {
            let current = nums[i % nums.len()];
            while let Some((last_index, last)) = stack.pop() {
                if last < current {
                    answer[last_index] = current;
                } else {
                    stack.push((last_index, last));
                    break;
                }
            }
        
            stack.push((i % nums.len(), current));
        }
        return answer;
    }
}