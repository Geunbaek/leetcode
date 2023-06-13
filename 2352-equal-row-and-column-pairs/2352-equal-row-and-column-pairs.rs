impl Solution {
    pub fn is_equal(grid: &Vec<Vec<i32>>, col:usize, row:usize, n:usize) -> bool {
        for i in 0..n {
            if grid[row][i] != grid[i][col] {
                return false
            }
        }
        return true;
    }
    
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut answer = 0;
        
        for y in 0..n {
            for x in 0..n {
                if Solution::is_equal(&grid, x, y, n) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}