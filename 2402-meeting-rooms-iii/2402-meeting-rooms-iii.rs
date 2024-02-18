use std::{collections::BinaryHeap, cmp};

impl Solution {
    pub fn most_booked(n: i32, meetings: Vec<Vec<i32>>) -> i32 {
        let mut meetings = meetings.clone();
        let mut unused_rooms: BinaryHeap<i32> = (0..n).map(|x| -x).collect();
        let mut used_rooms: BinaryHeap<(isize, i32)> = BinaryHeap::new();
        let mut count = vec![0_i32; n as usize];
        
        meetings.sort();

        for meeting in meetings {
            let (start, end) = (meeting[0] as isize, meeting[1] as isize);
            
            while !used_rooms.is_empty() && -used_rooms.peek().unwrap().0 <= start {
                let (_, room) = used_rooms.pop().unwrap();
                unused_rooms.push(room);
            }
            
            if let Some(room) = unused_rooms.pop() {
                used_rooms.push((-end, room));
                count[-room as usize] += 1;
            } else {
                if let Some((time, room)) = used_rooms.pop() {
                    let time = -time;
                    used_rooms.push((-(time + end - start), room));
                    count[-room as usize] += 1;
                } else {
                    break
                }
            }
        }
        
        let mut max = -1;
        let mut answer = -1;
        for i in 0..n {
             if max < count[i as usize] {
                 max = count[i as usize];
                 answer = i;
            }
        }
        return answer;
    }
}