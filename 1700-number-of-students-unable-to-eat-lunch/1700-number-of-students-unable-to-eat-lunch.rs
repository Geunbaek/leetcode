use std::collections::VecDeque;

impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let mut count = 0;
        let mut q = VecDeque::from(students);
            
        for (i, sandwich) in sandwiches.into_iter().enumerate() {
            let n = q.len();
            while count < n && sandwich != *q.front().unwrap() {
                let front = q.pop_front().unwrap();
                q.push_back(front);
                count += 1;
            }
            
            if *q.front().unwrap() == sandwich {
                q.pop_front();
            }
            if count == n {
                return n as i32;
            }
            count = 0;
        }
        0
    }
}