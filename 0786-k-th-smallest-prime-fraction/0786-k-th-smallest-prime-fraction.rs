impl Solution {
    pub fn kth_smallest_prime_fraction(arr: Vec<i32>, k: i32) -> Vec<i32> {
        let n = arr.len();
        
        let mut nums: Vec<(f64, i32, i32)> = vec![];
        
        for y in 0..n {
            for x in y + 1..n {
                let up = arr[y] as f64;
                let down = arr[x] as f64;
                nums.push((up / down, arr[y], arr[x]));
            }
        }
        
        nums.sort_by(|a, b| a.partial_cmp(b).unwrap());
        
        let (num, y, x) = nums[(k - 1) as usize];
        return vec![y, x];
    }
}