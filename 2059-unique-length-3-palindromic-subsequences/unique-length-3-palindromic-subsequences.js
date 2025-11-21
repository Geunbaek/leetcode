/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    const n = s.length;
    const prefix = Array.from({length: n + 1}, () => new Array(26).fill(0));

    for (let y = 1; y < n + 1; y++) {
        const char = s[y - 1];
        for (let x = 0; x < 26; x++) {
            if (char.charCodeAt(0) - 'a'.charCodeAt(0) === x) {
                prefix[y][x] = prefix[y - 1][x] + 1;
            } else {
                prefix[y][x] = prefix[y - 1][x];
            }
        }
    }

    const cache = new Set()
    for (let y = 1; y < n - 1; y++) {
        const char = s[y];
        for (let x = 0; x < 26; x++) {
            const sideChar = String.fromCharCode(x + 'a'.charCodeAt(0));
            if (cache.has(`${char}-${sideChar}`)) continue;
            if (prefix[y][x] - prefix[0][x] !== 0 && prefix[n][x] - prefix[y + 1][x] !== 0) cache.add(`${char}-${sideChar}`);
        }
    }
    return cache.size;
};