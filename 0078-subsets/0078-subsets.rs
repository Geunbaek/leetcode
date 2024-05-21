impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn get_subsets(n: usize, nums: &Vec<i32>, subsets: &mut Vec<Vec<i32>>, depth: usize, subset: &Vec<i32>) {
            if depth > n {
                return;
            }
            
            subsets.push(subset.to_vec());
            for i in depth..n {
                get_subsets(n, nums, subsets, i + 1, &[subset.to_vec(), vec![nums[i]]].concat());
            }
        }
        let n = nums.len();
        let mut subsets: Vec<Vec<i32>> = vec![];
        get_subsets(n, &nums, &mut subsets, 0, &vec![]);
        return subsets;
    }
}