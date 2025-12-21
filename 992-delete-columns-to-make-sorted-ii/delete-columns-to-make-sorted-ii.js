/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    const isSorted = (chars) => chars.every((char, i, cs) => i === 0 ? true : char >= cs[i - 1]);

    const r = strs.length;
    const c = strs[0].length;
    let answer = 0;
    let current = [];
    for (let x = 0; x < c; x++) {
        const chars = strs.map(str => str[x]);  
        const temp = chars.map((char, i) => (current[i] || "") + char);
        
        if (isSorted(temp)) {
            current = temp;
        } else {
            answer++;
        }
    }
    return answer;
};