use std::cmp;

impl Solution {
    pub fn max_consecutive_answers(answer_key: String, k: i32) -> i32 {
        let mut f_prefix: Vec<usize> = vec![0];       
        let mut t_prefix: Vec<usize> = vec![0];

        let n = answer_key.len();
        let k = k as usize;
        
        let key = answer_key.chars().collect::<Vec<char>>();
        
        for i in 0..n {
            if key[i] == 'T' {
                f_prefix.push(f_prefix[i]);
                t_prefix.push(t_prefix[i] + 1);
            } else {
                f_prefix.push(f_prefix[i] + 1);
                t_prefix.push(t_prefix[i]);
            }
        }
        
        
        let mut t_right = 0;
        let mut f_right = 0;
        let mut answer = 0;
        
        for left in 0..=n {
            while t_right < n + 1 && t_prefix[t_right] - t_prefix[left] <= k {
                t_right += 1;
            }
            answer = cmp::max(answer, t_right - left - 1);
            while f_right < n + 1 && f_prefix[f_right] - f_prefix[left] <= k {
                f_right += 1;
            }
            answer = cmp::max(answer, f_right - left - 1);
        }
        return answer as i32;
    }
}