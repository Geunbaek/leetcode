use std::collections::HashMap;

impl Solution {
    fn oper(cache: &HashMap<char, &str>, digits: &Vec<char>, path: &mut String, answer: &mut Vec<String>){
        if path.len() == digits.len() {
            answer.push(path.to_string());
            return;
        }
        
        let n = path.len();
        for c1 in cache[&digits[n]].chars() {
            path.push(c1);
            Solution::oper(cache, digits, path, answer);
            path.pop();
        }
    }
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits == String::new() {
            return vec![];
        }
        let mut digits: Vec<char> = digits.chars().collect();
        let cache: HashMap<char, &str> = HashMap::from([
            ('2', "abc"),
            ('3', "def"),
            ('4', "ghi"),            
            ('5', "jkl"),
            ('6', "mno"),
            ('7', "pqrs"),
            ('8', "tuv"),
            ('9', "wxyz")
        ]);
        let mut answer: Vec<String> = vec![];
        Solution::oper(&cache, &digits, &mut String::new(), &mut answer);
        return answer;
    }
}