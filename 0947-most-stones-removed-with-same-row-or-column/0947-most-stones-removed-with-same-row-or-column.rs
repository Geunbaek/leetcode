impl Solution {
    pub fn remove_stones(stones: Vec<Vec<i32>>) -> i32 {
        let size = stones.len();
        let mut parent:Vec<i32> = Vec::new();
        let mut ans = stones.len();
        
        for i in 0..size as i32 {
            parent.push(i);
        }
        
        fn find(p: &mut Vec<i32>, x: usize) -> i32{
            if p[x] != x as i32 {
                p[x] = find(p, p[x] as usize);
            }
            return p[x]
        }
        
        fn union(p: &mut Vec<i32>, a: usize, b: usize) {
            let ap = find(p, a) as usize;
            let bp = find(p, b);
            p[ap] = bp;
        }
        
        for i in 1..size {
            for j in 0..i {
                let left: &Vec<i32> = &stones[i];
                let right: &Vec<i32> = &stones[j];
                
                if left[0] == right[0] || left[1] == right[1] {
                    if find(&mut parent, i) != find(&mut parent, j) {
                        union(&mut parent, i, j);
                        ans -= 1;
                    }
                }
            }
        }
        return size as i32 - ans as i32;
        
    }
}