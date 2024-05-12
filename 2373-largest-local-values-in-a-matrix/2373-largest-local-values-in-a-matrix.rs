impl Solution {
    fn get_max_value(grid: &Vec<Vec<i32>>, x1: usize, y1: usize) -> i32 {
        let mut max = 0;
        for y in y1..y1 + 3 {
            for x in x1..x1 + 3 {
                max = max.max(grid[y][x]);
            }
        }
        max
    }
    
    pub fn largest_local(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len();
        
        let mut answer: Vec<Vec<i32>> = vec![vec![0; n - 2]; n - 2];
        
        for y in 0..=n - 3 {
            for x in 0..=n - 3 {
                answer[y][x] = Solution::get_max_value(&grid, x, y);
            }
        }
        answer
    }
}