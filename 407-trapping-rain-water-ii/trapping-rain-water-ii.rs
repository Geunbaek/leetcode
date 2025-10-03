
use std::collections::{BinaryHeap, HashSet};
use std::cmp::Reverse;

impl Solution {
    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        let r = height_map.len();
        let c = height_map[0].len();
        
        // BinaryHeap는 max heap이므로 Reverse로 감싸서 min heap으로 사용
        let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
        let mut water = 0;
        
        let dx = [-1, 0, 1, 0];
        let dy = [0, -1, 0, 1];
        
        let mut visited: HashSet<(usize, usize)> = HashSet::new();
        
        // 상단과 하단 경계 추가
        for x in 0..c {
            heap.push(Reverse((height_map[0][x], 0, x)));
            heap.push(Reverse((height_map[r - 1][x], r - 1, x)));
            visited.insert((0, x));
            visited.insert((r - 1, x));
        }
        
        // 좌측과 우측 경계 추가
        for y in 0..r {
            heap.push(Reverse((height_map[y][0], y, 0)));
            heap.push(Reverse((height_map[y][c - 1], y, c - 1)));
            visited.insert((y, 0));
            visited.insert((y, c - 1));
        }
        
        while let Some(Reverse((height, y, x))) = heap.pop() {
            for i in 0..4 {
                let nx = x as i32 + dx[i];
                let ny = y as i32 + dy[i];
                
                // 경계 체크
                if nx < 0 || nx >= c as i32 || ny < 0 || ny >= r as i32 {
                    continue;
                }
                
                let nx = nx as usize;
                let ny = ny as usize;
                
                // 방문 체크
                if visited.contains(&(ny, nx)) {
                    continue;
                }
                
                let next_height = height_map[ny][nx];
                
                // 물이 고일 수 있는 경우
                if next_height < height {
                    water += height - next_height;
                }
                
                visited.insert((ny, nx));
                heap.push(Reverse((next_height.max(height), ny, nx)));
            }
        }
        
        water
    }
}