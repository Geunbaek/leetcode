/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    return function(...args) {
        const stringArgs = args.toString()
        if (cache.has(stringArgs)){
            return cache.get(stringArgs)
        }
        cache.set(stringArgs, fn(...args));
        return cache.get(stringArgs);
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */