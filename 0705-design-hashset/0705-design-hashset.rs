use std::collections::HashSet;

struct MyHashSet {
    set: HashSet<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {

    fn new() -> Self {
        MyHashSet{
            set: HashSet::new(),
        }
    }
    
    fn add(&mut self, key: i32) {
        self.set.insert(key);
    }
    
    fn remove(&mut self, key: i32) {
        self.set.remove(&key);
    }
    
    fn contains(&self, key: i32) -> bool {
        self.set.contains(&key)
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet::new();
 * obj.add(key);
 * obj.remove(key);
 * let ret_3: bool = obj.contains(key);
 */