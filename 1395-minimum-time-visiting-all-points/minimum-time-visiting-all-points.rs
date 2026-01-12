use std::cmp;

impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        fn get_dist(p1: &Vec<i32>, p2: &Vec<i32>) -> i32 {
            let [x, y] = p1[..] else { todo!() };
            let [nx, ny] = p2[..] else { todo!() };
            cmp::max(x.abs_diff(nx), y.abs_diff(ny)) as i32
        }

        let n: usize = points.len();
        let mut dist: i32 = 0;
        for i in 1..n {
            dist += get_dist(&points[i - 1], &points[i]);
        }

        dist
    }
}