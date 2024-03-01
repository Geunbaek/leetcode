impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let n = s.len();
        let mut one_count = -1;
        let mut vec_s = vec![String::from("0"); n];
        vec_s[n - 1] = String::from("1");
        
        for c in s.chars() {
            if c == '1' {
                one_count += 1;
            }
        }
        
        if one_count == 0 {
            return vec_s.join("");
        }
        
        for i in 0..one_count as usize {
            vec_s[i] = String::from("1");
        }
        return vec_s.join("");
    }
}