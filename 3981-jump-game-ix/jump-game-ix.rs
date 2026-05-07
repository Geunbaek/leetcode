impl Solution {
    pub fn max_value(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();

        let mut ans = vec![0; n];
        let mut prev_max = vec![(0, 0_isize); n];

        let mut prev = (std::i32::MIN, -1_isize);
        for (i, &value) in nums.iter().enumerate() {
            if value > prev.0 {
                prev = (value, i as isize);
            }
            prev_max[i] = prev;
        }

        fn process(
            r: isize,
            right_min: i32,
            right_max: i32,
            nums: &[i32],
            prev_max: &[(i32, isize)],
            ans: &mut [i32],
        ) {
            let (p_max, pivot_index) = prev_max[r as usize];
            let curr_max = if p_max <= right_min { p_max } else { right_max };

            let mut next_right_min = p_max.min(right_min);
            for i in pivot_index..=r {
                ans[i as usize] = curr_max;
                next_right_min = next_right_min.min(nums[i as usize]);
            }

            if pivot_index == 0 {
                return;
            }

            process(pivot_index - 1, next_right_min, curr_max, nums, prev_max, ans);
        }

        process((n - 1) as isize, std::i32::MAX, 0, &nums, &prev_max, &mut ans);

        ans
    }
}