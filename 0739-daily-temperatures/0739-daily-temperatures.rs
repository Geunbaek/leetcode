impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n = temperatures.len();
        let mut stack: Vec<(i32, i32)> = vec![];
        let mut answer: Vec<i32> = vec![0; n];
        
        for (index, temperature) in temperatures.iter().enumerate() {
            while !stack.is_empty() && stack.last().unwrap().0 < *temperature {
                let (temp, j) = stack.pop().unwrap();
                answer[j as usize] = index as i32 - j;
            }
            stack.push((*temperature, index as i32));
        }
        return answer;
    }
}