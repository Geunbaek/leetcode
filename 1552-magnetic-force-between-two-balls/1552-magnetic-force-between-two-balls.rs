impl Solution {
    pub fn max_distance(position: Vec<i32>, m: i32) -> i32 {
        let mut position = position.clone();
        position.sort();
        
        let (mut left, mut right) = (0, 1_000_000_000);
        
        while left <= right {
            let mid = left + (right - left) / 2;
            let mut count = 0;
            let mut prev = -1;
            
            for p in position.iter() {
                if prev == -1 {
                    prev = *p;
                    count += 1;
                    continue;
                }
                
                if *p - prev >= mid {
                    prev = *p;
                    count += 1;
                }
            }
            
            if count >= m {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        right
    }
}