impl Solution {
    pub fn matrix_score(grid: Vec<Vec<i32>>) -> i32 {
        let mut grid = grid.clone();
        let r = grid.len();
        let c = grid[0].len();
        
        for y in 0..r {
            if grid[y][0] != 0 {
                continue;
            }
            for x in 0..c {
                grid[y][x] = 1 - grid[y][x];
            }
        }
        
        for x in 1..c {
            let mut zero = 0;
            for y in 0..r {
                if grid[y][x] == 0 {
                    zero += 1;
                }
            }
            if zero > r - zero {
                for y in 0..r {
                    grid[y][x] ^= 1;
                }
            }
        }
        
        let mut ans = 0;
        
        for l in grid.iter() {
            println!("{l:?}");
        }
        for y in 0..r {
            for x in 0..c {
                let col = grid[y][x] << (c - x - 1);
                ans += col;
            }
        }
        ans
    }
}