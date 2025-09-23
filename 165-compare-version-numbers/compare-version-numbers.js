const compare = (a, b) => a === b ? 0 : a > b ? 1 : -1

/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    const v1 = version1.split(".").map(Number);
    const v2 = version2.split(".").map(Number);

    const max = Math.max(v1.length, v2.length);

    for (let i = 0; i < max; i++) {
        const result = compare(v1[i] || 0, v2[i] || 0)
        if (result === 0) continue
        return result;
    }
    return 0;
};