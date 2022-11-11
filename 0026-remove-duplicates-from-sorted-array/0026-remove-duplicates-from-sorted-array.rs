impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut ans: usize = 1;
        for i in 1..nums.len(){
            if nums[i] != nums[i - 1]{
                nums[ans] = nums[i];
                ans += 1;
            }
        }
        return ans as i32;
    }
}