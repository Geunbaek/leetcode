/**
 * @param {number[]} complexity
 * @return {number}
 */
var countPermutations = function(complexity) {
    const MOD = 1_000_000_007;
    const n = complexity.length;
    const [root] = complexity;
    if (!(complexity.slice(1, n).every(c => c > root))) return 0;
    
    return Array
            .from({length: n - 2}, (_, i) => i + 2)
            .reduce((acc, cur) => acc * cur % MOD, 1)
};