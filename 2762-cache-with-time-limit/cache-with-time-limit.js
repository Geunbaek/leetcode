var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    if (this.cache.has(key)) {
        const prev = this.cache.get(key);
        if (Date.now() - prev.startedAt < prev.duration) {
            this.cache.set(key, { value, duration, startedAt: Date.now() })
            return true;
        }
    }

    this.cache.set(key, { value, duration, startedAt: Date.now() })
    return false;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
     if (this.cache.has(key)) {
        const prev = this.cache.get(key);
        if (Date.now() - prev.startedAt < prev.duration) {
            return prev.value;
        }
    }
    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let count = 0;

    for (const [key, value] of this.cache) {
        if (Date.now() - value.startedAt < value.duration) {
            count += 1;
        }
    }
    return count;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */