/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    if (o1 === o2) return true;
    if (typeof o1 !== typeof o2) return false;
    if (Array.isArray(o1) !== Array.isArray(o2)) return false;
    if (!o1 || !o2) return o1 === o2;
    if (
        typeof o1 === "boolean" || 
        typeof o1 === "number" || 
        typeof o1 === "string" ||
        typeof o1 === "null" ||
        typeof o1 === "undefined"
    ) return o1 === o2;

    const keys1 = Object.keys(o1);
    const keys2 = Object.keys(o2);

    if (keys1.length !== keys2.length) return false;

    let isEqual = true;
    for (const key of keys2) {
        if (!Reflect.has(o2, key)) return false;

        const value1 = o1[key];
        const value2 = o2[key];
        isEqual &= areDeeplyEqual(value1, value2);
    }
    return isEqual;
};