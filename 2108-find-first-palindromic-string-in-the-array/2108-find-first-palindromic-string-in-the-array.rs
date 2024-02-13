impl Solution {
    pub fn first_palindrome(words: Vec<String>) -> String {
        fn is_palindrome(word: &String) -> bool {
            let word_vec: Vec<char> = word.chars().collect();
            
            let (mut left, mut right) = (0_usize, word.len() - 1);
            
            while left < right {
                if word_vec[left] == word_vec[right] {
                    left += 1;
                    right -= 1;
                } else {
                    return false;
                }
            }
            return true;
        }
        
        for word in words.into_iter() {
            if is_palindrome(&word) {
                return word;
            }
        }
        return String::from("");
    }
}