impl Solution {
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals = intervals;
        intervals.sort_by(|a, b| a[1].cmp(&b[1]));
        
        let mut time: i32 = i32::MIN;
        let mut answer = 0;
        
        for interval in intervals.iter() {
            let u = interval[0];
            let v = interval[1];
            
            if u >= time {
                time = v;
            } else{
                answer += 1;
            }
            
        }
        return answer;
        
    }
}