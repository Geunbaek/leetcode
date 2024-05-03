impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let mut version1:Vec<i32> = version1.split(".").map(|x| x.parse::<i32>().unwrap()).collect();
        let mut version2:Vec<i32> = version2.split(".").map(|x| x.parse::<i32>().unwrap()).collect();
        
        let n = version1.len();
        let m = version2.len();
        let max = std::cmp::max(n, m);
        
        for i in 0..max {
            if i >= n {
                if version2[i] != 0 {
                    return -1;
                }
                continue;
            }
            
            if i >= m {
                if version1[i] != 0 {
                    return 1;
                }
                continue;
            }
            if version1[i] > version2[i] {
                return 1;
            } else if version1[i] < version2[i] {
                return -1;
            }
        }
        0
    }
}