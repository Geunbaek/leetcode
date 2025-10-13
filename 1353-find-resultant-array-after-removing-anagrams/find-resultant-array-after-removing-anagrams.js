const getAnagram = (word) => {
    return [...word].sort().join("");
}

/**
 * @param {string[]} words
 * @return {string[]}
 */
var removeAnagrams = function(words) {
    const stack = []

    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        const anagram = getAnagram(word);
        if (stack.length !== 0 && stack.at(-1).anagram === anagram) {
            continue
        } else {
            stack.push({ word, anagram });
        }
    }

    return stack.map(info => info.word);
};