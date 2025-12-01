const sum = (arr) => arr.reduce((acc, num) => acc + num, 0);


/**
 * @param {number} n
 * @param {number[]} batteries
 * @return {number}
 */
var maxRunTime = function(n, batteries) {
    let [l, r] = [0, Math.floor(sum(batteries) / n) + 1];

    while (l <= r) {
        const mid = Math.floor((l + r) / 2);

        let extra = 0;
        for (const battery of batteries) {
            extra += Math.min(battery, mid);
        }

        if (Math.floor(extra / n) >= mid) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return l - 1
};