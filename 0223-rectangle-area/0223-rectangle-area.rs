fn getRange(ax1:i32, ax2:i32, bx1:i32, bx2:i32) -> i32{
    if ax1 <= bx1 && bx1 <= bx2 && bx2 <= ax2 { 
        return bx2 - bx1;
    } 
    if ax1 <= bx1 && bx1 <= ax2 && ax2 <= bx2 {
        return ax2 - bx1;
    } 
    if bx1 <= ax1 && ax1 <= bx2 && bx2 <= ax2 {
        return bx2 - ax1;
    }
    if bx1 <= ax1 && ax1 <= ax2 && ax2 <= bx2 {
        return ax2 - ax1;
    }
    0
}

impl Solution {
    pub fn compute_area(ax1: i32, ay1: i32, ax2: i32, ay2: i32, bx1: i32, by1: i32, bx2: i32, by2: i32) -> i32 {
        let rect1 = (ax2 - ax1) * (ay2 - ay1);
        let rect2 = (bx2 - bx1) * (by2 - by1);
        let rect3 = getRange(ax1, ax2, bx1, bx2) * getRange(ay1, ay2, by1, by2);
        
        return rect1 + rect2 - rect3;
    }
}