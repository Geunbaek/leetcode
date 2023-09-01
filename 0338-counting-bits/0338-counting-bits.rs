impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut answer:Vec<i32> = vec![];
        
        for i in 0..=n {
            let bin = format!("{i:b}");
            let mut count = 0;
            for c in bin.chars() {
                if c == '1' {
                    count += 1;
                }
            }
            answer.push(count);
        }
        return answer;
    }
}