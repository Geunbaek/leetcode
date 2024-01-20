impl Solution {
    pub fn sum_subarray_mins(mut arr: Vec<i32>) -> i32 {
        let mut stack: Vec<isize> = vec![-1];
        let mut ans: isize = 0;
        arr.push(-1);
        
        for (i, num) in arr.iter().enumerate() {
            while stack.len() > 1 && arr[*stack.last().unwrap() as usize] >= *num {
                let mut last = stack.pop().unwrap();
                ans += arr[last as usize] as isize * (last - *stack.last().unwrap()) * (i as isize - last);
            }
            stack.push(i as isize);
            ans %= 1_000_000_007;
        }
        
        ans as i32
        
    }
}
