const isVowel = (alpha) => ['a', 'e', 'i', 'o', 'u'].includes(alpha.toLowerCase())

/**
 * @param {string} s
 * @return {string}
 */
var sortVowels = function(s) {
    const chars = s
        .split("")
        .filter(isVowel)
        .sort();
    let i = 0;
    return s
        .split("")
        .map(char => isVowel(char) ? chars[i++] : char)
        .join("")
};