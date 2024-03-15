impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        
        let mut l = vec![1];
        let mut r = vec![1];
        
        let mut answer = vec![];
        
        for i in 0..n {
            let mul = l[i] * nums[i];
            l.push(mul);
        }
        
        for i in (0..n).rev() {
            let mul = r[n - i - 1] * nums[i];
            r.push(mul);
        }
   
        for i in 1..=n {
            let left = l[i - 1] / l[0];
            let right = r[n - i] / r[0];
            answer.push(left * right);
        }
        answer
    }
}