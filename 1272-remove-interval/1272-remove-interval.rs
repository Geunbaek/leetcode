impl Solution {
    pub fn remove_interval(intervals: Vec<Vec<i32>>, to_be_removed: Vec<i32>) -> Vec<Vec<i32>> {
        fn remove_interval(s: i32, e: i32, cs: i32, ce: i32) -> Vec<Vec<i32>> {
            if s <= cs && cs < ce && ce <= e {
                if s == cs && ce == e {
                    return vec![];
                } else if s == cs {
                    return vec![vec![ce, e]];
                } else if e == ce {
                    return vec![vec![s, cs]];
                }
                return vec![vec![s, cs], vec![ce, e]];
            } else if s < e && e <= cs && cs < ce {
                return vec![vec![s, e]];
            } else if cs < ce && ce <= s && s < e {
                return vec![vec![s, e]];
            } else if cs <= s && s < e && e <= ce {
                return vec![];
            } else if s <= cs && cs <= e && e <= ce {
                return vec![vec![s, cs]];
            } else if cs <= s && s <= ce && ce <= e {
                return vec![vec![ce, e]];
            } else {
                return vec![];
            }
        }
        
        
        let mut answer: Vec<Vec<i32>> = vec![];
        let (cs, ce) = (to_be_removed[0], to_be_removed[1]);
        for interval in intervals {
            let (start, end) = (interval[0], interval[1]);
            let mut result = remove_interval(start, end, cs, ce);
            answer.append(&mut result);
        }
        answer
    }
}