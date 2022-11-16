/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * unsafe fn guess(num: i32) -> i32 {}
 */

impl Solution {
    unsafe fn guessNumber(n: i32) -> i32 {
        let mut left: i32 = 0;
        let mut right: i32 = n;
        let mut answer: i32 = 0;
        
        while &left <= &right {
            let mid = left + (right - left) / 2;
            println!("{} {}, {}", left, right, mid);
            let value = guess(mid);
    
            if value == -1 {
                right = mid - 1;
            } else if value == 1 {
                left = mid + 1;
            } else {
                answer = mid;
                break;
            }
        }
        return answer;
    }
}