impl Solution {
    pub fn min_speed_on_time(dist: Vec<i32>, hour: f64) -> i32 {
        let mut left = 1;
        let mut right:isize = 10_000_000_000;
        let mut answer:isize = 10_000_000_001;
        
        while left <= right {
            let mid:isize = left + (right - left) / 2;
            let mut time: f64 = 0.0;
            
            for (i, d) in dist.iter().enumerate() {
                if i != dist.len() - 1 {
                    time += (*d as f64 / mid as f64).ceil();
                } else {
                    time += *d as f64 / mid as f64
                }
            }
            
            if time <= hour {
                right = mid - 1;
                answer = std::cmp::min(answer, mid);
            } else {
                left = mid + 1;
            }
        }
        if answer == 10_000_000_001 {
            return -1
        } 
        return answer as i32;
    }
}

