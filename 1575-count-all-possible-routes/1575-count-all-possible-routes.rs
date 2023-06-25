use std::collections::HashMap;

impl Solution {
    pub fn oper(n: usize, locations: &Vec<i32>, memo: &mut HashMap<(i32, i64), i64>, cur_city: i32, fuel: i64, finish: i32) -> i64 {
        if fuel < 0 {
            return 0;
        }
        
        if memo.contains_key(&(cur_city, fuel)) {
            return *memo.get(&(cur_city, fuel)).unwrap();
        }
        
        let mut ret:i64 = 0;
        if cur_city == finish {
            ret = 1;
        }
        
        for next in 0..n {
            if next as i32 == cur_city { continue; }
            let next_fuel:i64 = fuel - ((locations[cur_city as usize] - locations[next]).abs() as i64);
            ret = (ret + Solution::oper(n ,locations, memo, next as i32, next_fuel, finish)) % 1_000_000_007;
        }
        
        memo.insert((cur_city, fuel), ret);
        return ret;
    }
    
    pub fn count_routes(locations: Vec<i32>, start: i32, finish: i32, fuel: i32) -> i32 {
        let n = locations.len();
        
        let mut memo: HashMap<_, _> = HashMap::new();
        
        return Solution::oper(n, &locations, &mut memo, start, fuel as i64, finish) as i32;
    }
}