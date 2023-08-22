
impl Solution {
    pub fn convert_to_title(column_number: i32) -> String {
        let mut column_number = column_number;
        let mut answer: Vec<u8> = vec![];

        while column_number > 0 {
            column_number -= 1;
            answer.push(65 + (column_number % 26) as u8);
            column_number /= 26;
        }
        
        answer.reverse();
        return String::from_utf8(answer).unwrap();
    }
}