impl Solution {
    pub fn min_moves_to_seat(seats: Vec<i32>, students: Vec<i32>) -> i32 {
        let mut seats = seats.clone();
        let mut students = students.clone();
        
        seats.sort();
        students.sort();
        
        let n = seats.len();
        let mut answer = 0;
        
        for i in 0..n {
            answer += seats[i].abs_diff(students[i]) as i32;
        }
        
        answer
    }
}