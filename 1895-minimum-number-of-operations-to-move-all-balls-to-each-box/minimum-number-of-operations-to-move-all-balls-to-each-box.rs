impl Solution {
    pub fn min_operations(boxes: String) -> Vec<i32> {
        let n = boxes.len();
        let mut answer: Vec<i32> = vec![0; n];
        let chars_vec: Vec<char> = boxes.chars().collect();

        for i in 0..n {
            for j in 0..n {
                if i == j {continue};
                if chars_vec[j] != '1' {continue };

                if i >= j {
                    answer[i] += (i - j) as i32;
                } else {
                    answer[i] += (j - i) as i32;
                }
            }
        }
        answer
    }
}

