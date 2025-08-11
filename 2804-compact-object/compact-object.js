/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (!obj) return;
    if (Array.isArray(obj)) {
        const ret = [];
        for (const el of obj) {
            const result = compactObject(el);
            if (!result) continue;
            ret.push(compactObject(el));
        }
        return ret;
    } else if (typeof obj === "object") {
        const ret = {};
        for (const [key, value] of Object.entries(obj)) {
            const result = compactObject(value);
            if (!result) continue;
            ret[key] = result;
        }
        return ret;
    } else {
        return obj;
    }
};