impl Solution {
    fn comb(n:usize, k: usize, index:usize, visited:&mut Vec<i32>, answer: &mut Vec<Vec<i32>>, path: Vec<i32>){
        if k == 0 {
            answer.push(path);
            return;
        }
        
        for i in index..n+1 {
            visited[i] = 1;
            let mut new = path.clone();
            new.push(i as i32);
            Solution::comb(n, k - 1, i+1, visited, answer, new);
            visited[i] = 0;
        }
        
    }
    
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let n = n as usize;
        let k = k as usize;
        
        let mut answer:Vec<Vec<i32>> = vec![];
        let mut visited:Vec<i32> = vec![0; n + 1];
        
        Solution::comb(n, k, 1, &mut visited, &mut answer, vec![]);
        return answer;
    }
}