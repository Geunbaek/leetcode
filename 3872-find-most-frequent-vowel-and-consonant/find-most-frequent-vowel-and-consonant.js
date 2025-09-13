/**
 * @param {string} s
 * @return {number}
 */
var maxFreqSum = function(s) {
    const vowols = [...'aeiou'].map(char => char.charCodeAt(0) - "a".charCodeAt(0));
    const counter = [...s]
        .reduce((acc, char) => {
            acc[char.charCodeAt(0) - "a".charCodeAt(0)]++;
            return acc;
        }, new Array(26).fill(0));
    return Math.max(...vowols.map(vowol => counter[vowol])) 
        + Math.max(...counter.map((cnt, alpha) => !vowols.includes(alpha) ? cnt : 0));
};