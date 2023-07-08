impl Solution {
    pub fn put_marbles(weights: Vec<i32>, k: i32) -> i64 {
        let n = weights.len();
        let m = n - 1;
        let k = k as usize;
        let mut pair_sum: Vec<i32> = vec![];
        
        let mut answer: i64 = 0;
        
        for i in 0..n-1 {
            pair_sum.push(weights[i] + weights[i + 1]);
        }
        
        pair_sum.sort();
    
        for i in 0..k-1 {
            answer += pair_sum[m - 1 - i] as i64;
        }
        
        for i in 0..k-1 {
            answer -= pair_sum[i] as i64;
        }
        
        answer
    }
}