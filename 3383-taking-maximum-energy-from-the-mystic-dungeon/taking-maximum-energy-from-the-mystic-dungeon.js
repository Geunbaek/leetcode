/**
 * @param {number[]} energy
 * @param {number} k
 * @return {number}
 */
var maximumEnergy = function(energy, k) {
    const prefixSum = Array.from({length: k}, (_, i) => energy[i]);

    for (let i = k; i < energy.length; i++) {
        prefixSum.push(prefixSum[i - k] + energy[i]);
    }

    let max = -Infinity;
    for (let i = 1; i <= k; i++) {
        let end = energy.length - i;

        max = Math.max(max, prefixSum[end]);

        let j = end - k;

        while (j >= 0) {
            max = Math.max(max, prefixSum[end] - prefixSum[j]);
            j -= k;
        }
    } 
    return max;
};