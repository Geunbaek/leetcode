impl Solution {
    fn check(arr: &Vec<i32>, index: usize) -> &str {
        if index == 0 {
            return "inc";
        }
        if index == arr.len() - 1 {
            return "dec";
        }
        if arr[index - 1] < arr[index] && arr[index] > arr[index + 1] {
            return "mid";
        }
        if arr[index - 1] > arr[index] && arr[index] > arr[index + 1] {
            return "dec";
        }
        if arr[index - 1] < arr[index] && arr[index] < arr[index + 1] {
            return "inc";
        }   
        return "";
    }
    
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let (mut left, mut right) = (0_usize,arr.len() - 1 );
        let mut answer = 0_usize;
        
        while left <= right {
            let mid = left + (right - left) / 2;
            match Solution::check(&arr, mid) {
                "mid" => {
                    answer = mid;
                    left = mid + 1;
                }
                "inc" => {
                    left = mid + 1;
                }
                "dec" => {
                    right = mid - 1;
                }
                _ => {
                    break;
                }
            }
            
        }
        return answer as i32;
        
    }
}