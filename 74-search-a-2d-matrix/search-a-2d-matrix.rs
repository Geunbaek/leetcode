impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let r = matrix.len();
        let c = matrix[0].len();
        
        let mut left = 0_isize;
        let mut right = (r * c - 1) as isize;
        
        let mut answer = -1;
        while left <= right {
            let mut mid = (left + right) / 2;
            let x = (mid % c as isize) as usize;
            let y = (mid / c as isize) as usize;
   
            if matrix[y][x] < target {
                left = mid + 1;
            } else if matrix[y][x] > target {
                right = mid - 1;
            } else {
                answer = mid as i32;
                break;
            }
        }
        
        return answer >= 0;
    }
}