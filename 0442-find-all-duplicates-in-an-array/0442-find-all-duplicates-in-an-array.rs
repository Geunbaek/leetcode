impl Solution {
    pub fn find_duplicates(nums: Vec<i32>) -> Vec<i32> {
        let mut cache = vec![0; 100_001];
        let mut answer = vec![];
        
        for num in nums {
            let num = num as usize;
            cache[num] += 1;
            if cache[num] >= 2 {
                answer.push(num as i32);
            }
        }
        answer
    }
}