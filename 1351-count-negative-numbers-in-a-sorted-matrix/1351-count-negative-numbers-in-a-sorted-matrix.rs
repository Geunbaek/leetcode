impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let (r, c) = (grid.len(), grid[0].len());
        let mut answer = 0;
        for y in 0..r {
            for x in 0..c {
                if grid[y][x] < 0 {
                    answer += 1
                }
            }
        }
        answer
    }
}