/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    const goodNums = [];

    let count = 0;
    let prev = ""

    for (const char of num) {
        if (char === prev) {
            count += 1;
            if (count === 3) {
                goodNums.push(parseInt(char.repeat(3)));
                count = 0;
                prev = ""
            } 
        } else {
            prev = char;
            count = 1;
        }
    }

    if (goodNums.length === 0) return "";
    const max = Math.max(...goodNums);

    return max === 0 ? "000" : max.toString();
};