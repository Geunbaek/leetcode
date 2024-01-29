use std::collections::VecDeque;

struct MyQueue {
    q: VecDeque<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    fn new() -> Self {
        MyQueue {q: VecDeque::new()}
    }
    
    fn push(&mut self, x: i32) {
        self.q.push_back(x);
    }
    
    fn pop(&mut self) -> i32 {
        match self.q.pop_front() {
            Some(num) => return num,
            None => return 0,
        }
    }
    
    fn peek(&self) -> i32 {
        match self.q.front() {
            Some(num) => return *num,
            None => return 0,
        }
    }
    
    fn empty(&self) -> bool {
        return self.q.is_empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */