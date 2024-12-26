impl Solution {
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut answer = 0;

        fn recur(n: usize, depth: usize, value: i32, target: i32, answer: &mut i32, nums: &Vec<i32>) {
            if (depth >= n) {
                if (value == target) {
                    *answer += 1;
                }
                return;
            }

            recur(n, depth + 1, value + nums[depth], target, answer, nums);
            recur(n, depth + 1, value - nums[depth], target, answer, nums);
        }
        recur(n, 0, 0, target, &mut answer, &nums);
        return answer;
    }
}