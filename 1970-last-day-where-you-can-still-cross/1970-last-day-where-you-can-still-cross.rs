impl Solution {
    pub fn find(parent: &mut Vec<usize>, x: usize) -> usize {
        if parent[x] != x {
            parent[x] = Solution::find(parent, parent[x]);
        }
        return parent[x];
    }
    
    pub fn union(parent: &mut Vec<usize>, a: usize, b: usize){
        let a_parent = Solution::find(parent, a);
        let b_parent = Solution::find(parent, b);
        parent[a_parent] = b_parent;

    }
    
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        let r = row as usize;
        let c = col as usize;
        
        let mut parent: Vec<usize> = (0..(r * c + 2)).map(|x| x).collect();
        let mut board = vec![vec![0; c]; r];
        
        let dx:[isize;8] = [-1, -1, 0, 1, 1, 1, 0, -1];
        let dy:[isize;8] = [0, -1, -1, -1, 0, 1, 1, 1];
        
        for (day, cell) in cells.iter().enumerate() {
            let a = cell[0] as usize;
            let b = cell[1] as usize;
            let (y, x) = (a - 1, b - 1);
            let i = y * c + x + 1;
            board[y][x] = 1;
            
            for d in 0..8 {
                let nx = (x as isize + dx[d]) as usize;
                let ny = (y as isize + dy[d]) as usize;
                
                if !(0 <= nx && nx < c && 0 <= ny && ny < r) {
                    continue;
                }
                
                if board[ny][nx] == 0 {
                    continue;
                }

                let j = ny * c + nx + 1;
                Solution::union(&mut parent, i, j);
            }
            if x == 0 {
                Solution::union(&mut parent, 0, i);
            } else if x == c - 1 {
                Solution::union(&mut parent, i, r * c + 1);
            }
            
            if Solution::find(&mut parent, 0) == Solution::find(&mut parent, r * c + 1) {
                return day as i32;
            }
        }
        return -1;
    }
}