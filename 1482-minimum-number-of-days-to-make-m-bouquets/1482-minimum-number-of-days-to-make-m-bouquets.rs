impl Solution {
    pub fn min_days(bloom_day: Vec<i32>, m: i32, k: i32) -> i32 {
        let n = bloom_day.len() as i32;
        
        if n < m * k {
            return -1;
        }
        let max = 1_000_000_001;
        let mut left = 0;
        let mut right = 1_000_000_001;
        let mut answer = right;
        
        while left <= right {
            let mid = left + (right - left) / 2;
            
            let mut stack: Vec<(usize, i32)> = vec![];
            
            for (i, day) in bloom_day.iter().enumerate() {
                if *day > mid {
                    continue;
                }
                
                if let Some((last, count)) = stack.pop() {
                    if count >= k {
                        stack.push((last, count));
                        stack.push((i, 1));
                        continue;
                    }
                    if last + 1 < i {
                        stack.push((i, 1));
                        continue;
                    }
                    stack.push((i, count + 1));
                } else {
                    stack.push((i, 1));
                    continue;
                }
            }
            
            if let Some((last, count)) = stack.last() {
                if *count < k {
                    stack.pop();
                }
            }
            
            if stack.len() as i32 >= m {
                right = mid - 1;
                answer = std::cmp::min(answer, mid);
            } else {
                left = mid + 1;
            }
            
        }
        if answer == max {
            return -1;
        }
        answer
    }
}