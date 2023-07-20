impl Solution {
    pub fn answer(nums: &Vec<i32>, divisor: i32) -> i32 {
        let mut res: Vec<i32> = vec![0; nums.len()];

        for i in 0..nums.len() {
            res[i] = (nums[i] as f64 / divisor as f64).ceil() as i32;
        }

        return res.iter().sum::<i32>();
    }

    pub fn smallest_divisor(nums: Vec<i32>, threshold: i32) -> i32 {
        let mut left = 1;
        let mut right = 1_000_000;

        while left <= right {
            let mid = left + (right - left) / 2;
            
            let sum = Solution::answer(&nums, mid);

            if sum <= threshold {
                right = mid - 1;
            } else {
                left = mid + 1
            }
        }

        return left;
    }
}