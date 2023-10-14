impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut v = (cost[cost.len() - 2], cost[cost.len() - 1]);
    for i in (0 .. cost.len() - 2).rev() {
      v = (v.0.min(v.1) + cost[i], v.0);
    }
    return v.0.min(v.1);
    }
}