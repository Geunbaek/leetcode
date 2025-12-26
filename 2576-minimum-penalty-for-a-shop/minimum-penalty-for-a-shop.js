/**
 * @param {string} customers
 * @return {number}
 */
var bestClosingTime = function(customers) {
    const n = customers.length;
    const prefix_y = [0];
    const prefix_n = [0];
    for (let i = 0; i < n; i++) {
        prefix_y.push(prefix_y[i] + (customers[i] === "Y" ? 1 : 0));
        prefix_n.push(prefix_n[i] + (customers[i] === "N" ? 1 : 0));
    }

    let answer = n;
    let panalty = Infinity;
    for (let i = n; i >= 0; i--) {
        const now = prefix_y[n] - prefix_y[i] + (prefix_n[i] - prefix_n[0]);
        if (panalty >= now) {
            panalty = now
            answer = Math.min(answer, i);
        }
    }
    return answer;
};