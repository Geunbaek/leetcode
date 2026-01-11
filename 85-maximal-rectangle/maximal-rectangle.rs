impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        fn get_max_area(dp: &Vec<usize>) -> i32 {
            let n = dp.len() as i32;
            let mut stack: Vec<i32> = vec![-1];
            let mut max_area = 0;
            
            for i in 0..n {
                while *stack.last().unwrap() != -1 && dp[*stack.last().unwrap() as usize] >= dp[i as usize] {
                    let last = stack.pop().unwrap() as usize;
                    let area = dp[last] as i32 * (i - *stack.last().unwrap() - 1);
                    max_area = std::cmp::max(max_area, area);
                }
                stack.push(i);
            }
            while *stack.last().unwrap() != -1 {
                let last = stack.pop().unwrap() as usize;
                max_area = std::cmp::max(max_area, dp[last] as i32 * (dp.len() as i32 - *stack.last().unwrap() - 1));
            }
            max_area
        }
        
        let r = matrix.len();
        let c = matrix[0].len();
        
        let mut dp: Vec<usize> = vec![0; c];
        let mut answer = 0;
        
        for y in 0..r {
            for x in 0..c {
                if matrix[y][x] == '0' {
                    dp[x] = 0;
                } else {
                    dp[x] += 1;
                }
            }
            answer = std::cmp::max(answer, get_max_area(&dp));
        }
        answer as i32
    }
}