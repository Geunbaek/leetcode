impl Solution {
    pub fn max_run_time(n: i32, batteries: Vec<i32>) -> i64 {
        let mut left: i64 = 0;
        let mut right: i64 = 0;

        for battery in batteries.iter() {
            right += *battery as i64;
        }
        
        while left <= right {
            let mid = left + (right - left) / 2;
            
            let mut total:i64 = 0;
            
            for battery in batteries.iter() {
                total += std::cmp::min(*battery as i64, mid);    
            }
            
            if total / n as i64 >= mid {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right;
    }
}