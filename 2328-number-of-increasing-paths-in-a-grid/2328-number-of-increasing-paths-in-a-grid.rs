impl Solution {
    pub fn dfs(grid:&Vec<Vec<i32>>, dp:&mut Vec<Vec<i32>>, x:usize,y:usize,dx:&[isize;4],dy:&[isize;4])->i32{
        if dp[y][x] != 0 {
            return dp[y][x];
        }
        let mut ret = 1;
        for i in 0..4{
            let nx = ((x as isize) + dx[i]) as usize;
            let ny = ((y as isize) + dy[i]) as usize;
            if !(0 <= nx && nx < grid[0].len() && 0 <= ny && ny < grid.len()){ continue; }
            if grid[y][x] >= grid[ny][nx] {
                continue;
            }
            ret += Solution::dfs(grid, dp, nx, ny, dx, dy) % 1_000_000_007;
        }
        dp[y][x]=ret % 1_000_000_007;
        return ret;
    }
    pub fn count_paths(grid: Vec<Vec<i32>>) -> i32 {
        let (r,c) = (grid.len(),grid[0].len());
        let mut dp = vec![vec![0;c];r];
        let dx:[isize;4] = [-1,0,1,0];
        let dy:[isize;4] = [0,-1,0,1];
        
        for y in 0..r{
            for x in 0..c{
                Solution::dfs(&grid,&mut dp, x, y, &dx, &dy);
            }
        }
        let mut answer = 0;
        
        for y in 0..r{
            for x in 0..c{
                answer += dp[y][x];
                answer %= 1_000_000_007;
            }
        }
        answer % 1_000_000_007
    }
}