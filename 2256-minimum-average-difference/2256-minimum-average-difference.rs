impl Solution {
    pub fn minimum_average_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i64;
        let mut left: i64 = 0;
        let mut new_nums: Vec<i64> = nums.iter().map(|&num| num as i64).collect();
        let mut right: i64 = new_nums.iter().sum();
    
        let mut min: i64 = i64::MAX;;
        let mut answer = 0;
 
        for (i, num) in new_nums.iter().enumerate() {
            let m = i as i64 + 1;
            
            left += num;
            right -= num;

            let avg_diff: i64 = 
                if m != n {
                    ((left / m) - (right / (n - m))).abs()
                } else {
                    ((left / m) - 0).abs()
                };
            
            
            if min > avg_diff {
                min = avg_diff;
                answer = i as i32;
           }
        }
        answer
    }
}