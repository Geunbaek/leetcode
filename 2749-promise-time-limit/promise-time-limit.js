/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...arg) {
        const cancel = new Promise((_, reject) => setTimeout(() => reject("Time Limit Exceeded"), t));
        const oper = new Promise((resolve) => setTimeout(() => {
            resolve(fn(...arg))
        }, arg))
        return (await Promise.race([oper, cancel]))
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */