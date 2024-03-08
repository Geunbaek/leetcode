use std::collections::{HashMap};

impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut counter: HashMap<i32, usize> = HashMap::new();
        
        for num in nums {
            counter.entry(num).and_modify(|x| *x += 1).or_insert(1);
        }
        
        let mut answers: Vec<(usize, i32)> = vec![];
        for (num, count) in counter {
            answers.push((count, num));
        }
        
        answers.sort();
        
        let max = answers.last().unwrap().0;
        
        let mut answer = 0;
        
        while let Some((cnt, num)) = answers.pop() {
            if cnt == max {
                answer += cnt;
            }
        }
        return answer as i32;
    }
}