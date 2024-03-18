impl Solution {
    pub fn merge_points(point1: &Vec<i32>, point2: &Vec<i32>) -> Vec<Vec<i32>> {
        let (s1, e1) = (point1[0], point1[1]);
        let (s2, e2) = (point2[0], point2[1]);
        
        if s1 <= s2 && s2 <= e1 && e1 <= e2 {
            return vec![vec![s2, e1]];
        }
        
        if s1 <= s2 && s2 <= e2 && e2 <= e1 {
            return vec![vec![s2, e2]];
        }
        
        vec![vec![s1, e1], vec![s2, e2]]
    }
    
    pub fn find_min_arrow_shots(points: Vec<Vec<i32>>) -> i32 {
        let mut points = points.clone();
        points.sort();
        
        let mut answer = 0;
        while points.len() >= 2 {
            let first = points.pop().unwrap();
            let second = points.pop().unwrap();
            
            let mut merged_points = Solution::merge_points(&second, &first);
            if merged_points.len() == 1 {
                points.append(&mut merged_points);
            } else {
                answer += 1;
                points.push(second);
            }
        }
        answer + points.len() as i32
    }
}