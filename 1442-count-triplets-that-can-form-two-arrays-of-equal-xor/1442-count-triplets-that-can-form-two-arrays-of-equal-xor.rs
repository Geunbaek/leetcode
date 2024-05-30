impl Solution {
    pub fn count_triplets(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        
        let mut answer = 0;
        
        for left in 0..n {
            let mut a = arr[left];
            
            for mid in left + 1..n {
                a ^= arr[mid];
                
                let mut b = arr[mid];
                
                for right in mid..n {
                    b ^= arr[right];
                    if a == b {
                        answer += 1;
                    }
                }
            }
        }
        answer
    }
}