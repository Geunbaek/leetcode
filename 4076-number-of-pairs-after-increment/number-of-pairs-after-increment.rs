use std::collections::HashMap;

impl Solution {
    const SQRT: usize = 225;
    pub fn number_of_pairs(
        nums1: Vec<i32>,
        mut nums2: Vec<i32>,
        queries: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        let mut answer = Vec::new();
        
        let mut cnt: Vec<HashMap<i32, i32>> = vec![HashMap::new(); Self::SQRT];
        let mut sum: Vec<i32> = vec![0; Self::SQRT];

        for i in 0..nums2.len() {
            let block = i / Self::SQRT;
            if block < Self::SQRT {
                *cnt[block].entry(nums2[i]).or_insert(0) += 1;
            }
        }

        for query in queries {
            if query[0] == 1 {
                let s = query[1] as usize;
                let e = query[2] as usize;
                let val = query[3];

                let l = s / Self::SQRT;
                let r = e / Self::SQRT;

                if l == r {
                    for j in s..=e {
                        let block = j / Self::SQRT;
                        
                        if let Some(count) = cnt[block].get_mut(&nums2[j]) {
                            *count -= 1;
                        }
                        
                        nums2[j] += val;
                        
                        *cnt[block].entry(nums2[j]).or_insert(0) += 1;
                    }
                } else {
                    let l_end = (l + 1) * Self::SQRT;
                    for j in s..l_end {
                        let block = j / Self::SQRT;
                        if let Some(count) = cnt[block].get_mut(&nums2[j]) {
                            *count -= 1;
                        }
                        nums2[j] += val;
                        *cnt[block].entry(nums2[j]).or_insert(0) += 1;
                    }

                    for j in (l + 1)..r {
                        sum[j] += val;
                    }

                    let r_start = r * Self::SQRT;
                    for j in r_start..=e {
                        let block = j / Self::SQRT;
                        if let Some(count) = cnt[block].get_mut(&nums2[j]) {
                            *count -= 1;
                        }
                        nums2[j] += val;
                        *cnt[block].entry(nums2[j]).or_insert(0) += 1;
                    }
                }
            } else {
                let val = query[1];
                let mut ans = 0;

                for &num1 in &nums1 {
                    for k in 0..Self::SQRT {
                        let target = val - num1 - sum[k];
                        if let Some(&count) = cnt[k].get(&target) {
                            ans += count;
                        }
                    }
                }

                answer.push(ans);
            }
        }

        answer
    }
}