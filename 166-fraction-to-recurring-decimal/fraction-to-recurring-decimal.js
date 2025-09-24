
/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    if (numerator === 0) return "0";
    const fraction = [];

    if ((numerator < 0 && denominator >= 0) 
        || (numerator >= 0 && denominator < 0)) {
            fraction.push('-');
    }

    const divided = Math.abs(numerator);
    let divisor = Math.abs(denominator);
    let remainder = divided % divisor;
    fraction.push(Math.floor(divided / divisor).toString());
    
    if (remainder === 0) {
        return fraction.join("");
    }

    fraction.push(".");

    const cache = new Map();

    while (remainder !== 0) {
        if (cache.has(remainder)) {
            fraction.splice(cache.get(remainder), 0, "(");
            fraction.push(")");
            break;
        }

        cache.set(remainder, fraction.length);
        remainder *= 10;
        fraction.push(Math.floor(remainder / divisor).toString());
        remainder %= divisor;
    }
    
   return fraction.join("");
};