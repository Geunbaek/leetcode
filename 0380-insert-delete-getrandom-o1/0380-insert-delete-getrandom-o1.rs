use std::collections::HashSet;
use rand::Rng;

struct RandomizedSet {
    set: HashSet<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        Self { set: HashSet::new() }
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if self.set.contains(&val) {
            return false;
        }
        
        self.set.insert(val);
        true
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if self.set.contains(&val) {
            self.set.remove(&val);
            return true;
        }
        false
    }
    
    fn get_random(&self) -> i32 {
        let mut rng = rand::thread_rng();
        let index: usize = rng.gen_range(0,self.set.len());
        let mut count: usize = 0;
        for num in self.set.iter() {
            if count == index {
                return *num;
            }
            count += 1;
        }
        -1
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */