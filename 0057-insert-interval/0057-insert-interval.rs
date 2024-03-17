impl Solution {
    pub fn check_merge_interval(interval1: &Vec<i32>, interval2: &Vec<i32>) -> bool {
        let (s1, e1) = (interval1[0], interval1[1]);
        let (s2, e2) = (interval2[0], interval2[1]);
        if e1 < s2 {
            return false;
        }
        
        if s1 <= s2 && s2 <= e1 && e1 <= e2 {
            return true;
        }
        
        if s1 <= s2 && s2 <= e1 && e2 <= e1 {
            return true
        }
        
        false
    } 
    
    pub fn merge_interval(interval1: Vec<i32>, interval2: Vec<i32>) -> Vec<Vec<i32>> {
        let (s1, e1) = (interval1[0], interval1[1]);
        let (s2, e2) = (interval2[0], interval2[1]);
        if e1 < s2 {
            return vec![interval1, interval2];
        }
        
        if s1 <= s2 && s2 <= e1 && e1 <= e2 {
            return vec![vec![s1, e2]];
        }
        
        if s1 <= s2 && s2 <= e1 && e2 <= e1 {
            return vec![vec![s1, e1]];
        }
        
        vec![interval1, interval2]
    }
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut new_intervals = intervals.clone();
        new_intervals.push(new_interval);
        new_intervals.sort();
        
        let mut answer: Vec<Vec<i32>> = vec![];
        
        for interval in new_intervals {
            answer.push(interval);
            while answer.len() >= 2 && Solution::check_merge_interval(&answer[answer.len() - 2], &answer[answer.len() - 1]) {
                let last = answer.pop().unwrap();
                let second = answer.pop().unwrap();
                answer.append(&mut Solution::merge_interval(second, last))
            }
        }
        
        answer
    }
}