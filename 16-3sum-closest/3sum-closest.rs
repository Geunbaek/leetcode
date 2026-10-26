impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut closest_sum = nums[0] + nums[1] + nums[2];

        for i in 0..n {
            for j in (i + 1)..n {
                for k in (j + 1)..n {
                    let temp = nums[i] + nums[j] + nums[k];
                    if (target - closest_sum).abs() > (target - temp).abs() {
                        closest_sum = temp;
                    }
                }
            }
        }

        closest_sum
    }
}