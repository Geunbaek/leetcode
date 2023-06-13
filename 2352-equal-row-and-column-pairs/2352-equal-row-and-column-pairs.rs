impl Solution {
    pub fn get_row(grid: &Vec<Vec<i32>>, row: usize, c: usize) -> Vec<i32> {
        return (0..c).map(|i| grid[row][i]).collect();
    }
    pub fn get_col(grid: &Vec<Vec<i32>>, col: usize, r: usize) -> Vec<i32> {
        return (0..r).map(|i| grid[i][col]).collect();
    }
    pub fn is_equal(row: &Vec<i32>, col: &Vec<i32>) -> bool {
        for i in 0..row.len() {
            if row[i] != col[i] {
                return false;
            }
        }
        return true;
    }
    
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let (r, c) = (grid.len(), grid[0].len());
        let mut answer = 0;
        
        for y in 0..r {
            let row = Solution::get_row(&grid, y, c);
            for x in 0..c {
                let col = Solution::get_col(&grid, x, r);
                if Solution::is_equal(&row, &col) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}