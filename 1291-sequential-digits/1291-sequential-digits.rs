impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let mut digits: Vec<String> = (1..10).map(|x| x.to_string()).collect();
        let mut s_digits: Vec<i32> = vec![];
        
        for i in 0..9 {
            for j in i+1..9 {
                let digit = digits[i..j + 1].join("").parse::<i32>().unwrap();
                s_digits.push(digit);
            }
        }
        
        let mut ans = vec![];
        
        for digit in s_digits.iter() {
            if low <= *digit && *digit <= high {
                ans.push(*digit);
            }
        }
        ans.sort();
        ans
    }
}
                