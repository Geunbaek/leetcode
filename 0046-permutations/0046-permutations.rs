impl Solution {
    fn perm(n: usize, nums: &Vec<i32>, answer: &mut Vec<Vec<i32>>, path:&mut Vec<i32>) {
        if path.len() == n {
            answer.push(path[..].to_vec());
            return;
        }
        
        for num in nums.iter() {
            if path.contains(num) {
                continue;
            }
            path.push(*num);
            Solution::perm(n, nums, answer, path);
            path.pop();
        }
        
        
    }
    
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let n = nums.len();
        let mut answer: Vec<Vec<i32>> = vec![];
        
        Solution::perm(n, &nums, &mut answer, &mut vec![]);
        return answer;
    }
}