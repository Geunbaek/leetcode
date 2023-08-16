use std::collections::BinaryHeap;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut left = 0_usize;
        let mut right = (k - 1) as usize;
        
        let mut h: BinaryHeap<(i32, usize)> = BinaryHeap::new();
        
        for i in 0..k as usize {
            h.push((nums[i], i));
        }
        
//          while right < len(nums):
//             _max, index = h[0]
            
//             while index < left:
//                 heapq.heappop(h)
//                 _max, index = h[0]
                
//             answer.append(-_max)
//             left += 1
//             right += 1
//             if right >= len(nums):
//                 break
//             heapq.heappush(h, (-nums[right], right))
//         return answer
            
        
        let mut answer:Vec<i32> = vec![];
        
        while right < nums.len() {
            let mut peek = h.peek().unwrap();
            
            while peek.1 < left {
                h.pop();
                peek = h.peek().unwrap();
            }
            
            answer.push(peek.0);
            left += 1;
            right += 1;
            
            if right >= nums.len() {
                break;
            }
            h.push((nums[right], right));
        }
        return answer;
    }
}

            
