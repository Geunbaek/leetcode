use std::collections::HashMap;

impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        let mut cache: HashMap<i32, i32> = HashMap::new();
        let mut answer: Vec<i32> = vec![];
        let mut remain: Vec<i32> = vec![];
        
        for num in arr1 {
            cache.entry(num).and_modify(|x| *x += 1).or_insert(1);
        }
        
        for num in arr2 {
            let cnt = cache[&num];
            cache.entry(num).and_modify(|x| *x = 0).or_insert(0);
            for _ in 0..cnt {
                answer.push(num);
            }
        }
        
        for (key, value) in cache.iter() {
            if *value == 0 {
                continue;
            }
            for _ in 0..*value {
                remain.push(*key);
            }
        }
        
        remain.sort();
        return [answer, remain].concat();
    }
}