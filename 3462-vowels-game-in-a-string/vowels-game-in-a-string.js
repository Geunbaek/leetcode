/**
 * @param {string} s
 * @return {boolean}
 */
var doesAliceWin = function(s) {
    return [...s].some(char => 'aeiou'.includes(char))
};