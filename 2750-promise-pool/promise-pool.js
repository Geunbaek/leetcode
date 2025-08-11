/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
    const next = async (fn) => {
        if (!fn) return;
        await fn();
        await next(functions[n++]);
    }

    const promises = functions
        .slice(0, n)
        .map(next);

    return Promise.all(promises)
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */