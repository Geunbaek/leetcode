/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let timer;
    let lastArgs;
    let callCount;

    const tick = () => {
        if (callCount > 1) {
            fn(...lastArgs); 
            callCount = 1
            timer = setTimeout(tick, t)
        } else {
            timer = null
        }
    }

    return function(...args) {
        lastArgs = args;
        callCount += 1;

        if (timer) return;
     
        fn(...lastArgs);   
        callCount = 1    
        timer = setTimeout(tick, t);
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */