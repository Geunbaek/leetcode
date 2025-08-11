/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = null;
    return function() {
        if (count === null) {
            count = n;
        } else {
            count += 1
        }
        return count
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */