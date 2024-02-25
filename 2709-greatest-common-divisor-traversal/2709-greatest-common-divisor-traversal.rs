use std::collections::HashMap;

impl Solution {
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        fn find(p: &mut Vec<usize>, x: usize) -> usize {
            if p[x] != x {
                p[x] = find(p, p[x]);
            }
            p[x]
        }
        
        fn union(p: &mut Vec<usize>, size: &mut Vec<usize>, a: usize, b: usize) {
            let mut ap = find(p, a);
            let mut bp = find(p, b);
    
            if ap == bp {
                return;   
            }   
            
            if size[ap] < size[bp] {
                (ap, bp) = (bp, ap);
            }

            p[bp] = ap;
            size[ap] += size[bp];
        }
        
        
        let n = nums.len();
        
        if n == 1 {
            return true;
        }
        
        let mut p: Vec<usize> = (0..n).map(|x| x).collect();
        let mut size: Vec<usize> = vec![1; n];
        
        let mut first_occur: HashMap<usize, usize> = HashMap::new();
        
        
        for i in 0..n {
            let mut num = nums[i] as usize;
            let mut div = 2_usize;
            
            while div * div <= num {
                if num % div == 0 {
                    if first_occur.contains_key(&div) {
                        union(&mut p, &mut size, i, first_occur[&div]);
                    } else {
                        first_occur.insert(div, i);
                    }
                    while num % div == 0 {
                        num /= div;
                    }
                }
                div += 1;
            }
            
            if num > 1 {
                if first_occur.contains_key(&num) {
                    union(&mut p, &mut size, i, first_occur[&num]);
                } else {
                    first_occur.insert(num, i);
                }
            }
        }
        return size[find(&mut p, 0)] == n;
    }
}

