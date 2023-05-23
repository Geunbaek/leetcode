struct KthLargest {
    nums: Vec<i32>,
    k: usize
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {

    fn new(k: i32, nums: Vec<i32>) -> Self {
        Self {
            nums: nums,
            k: k as usize
        }
    }
    
    fn add(&mut self, val: i32) -> i32 {
        self.nums.push(val);
        self.nums.sort_by(|a, b| b.cmp(a));
        return self.nums[self.k - 1];
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest::new(k, nums);
 * let ret_1: i32 = obj.add(val);
 */