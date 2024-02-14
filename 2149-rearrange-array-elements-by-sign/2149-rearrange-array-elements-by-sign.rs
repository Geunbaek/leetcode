impl Solution {
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        let mut positive_nums: Vec<i32> = vec![];
        let mut negative_nums: Vec<i32> = vec![];
        
        for num in nums {
            if num < 0 {
                negative_nums.push(num);
            } else {
                positive_nums.push(num);
            }
        }
        
        let mut answer: Vec<i32> = vec![];
        
        for (positive_num, negative_num) in positive_nums.iter().zip(&negative_nums) {
            answer.push(*positive_num);
            answer.push(*negative_num);
        }
        answer
    }
}