/**
 * @param {number[]} prices
 * @param {number[]} strategy
 * @param {number} k
 * @return {number}
 */
var maxProfit = function(prices, strategy, k) {
    const n = prices.length;
    const prefixProfit = [0];
    const prefixPrice = [0];

    for (let i = 0; i < n; i++) {
        const p = prices[i];
        const s = strategy[i];
        prefixProfit.push(prefixProfit[i] + (p * s));
        prefixPrice.push(prefixPrice[i] + p);
    }

    let answer = prefixProfit[n];

    for (let i = k; i <= n; i ++) {
        const l = prefixProfit[i - k];
        const r = prefixProfit[n] - prefixProfit[i];
        const mid = prefixPrice[i] - prefixPrice[i - Math.floor(k / 2)];
        const modify = l + r + mid;
        answer = Math.max(answer, modify);
    } 
    return answer

};