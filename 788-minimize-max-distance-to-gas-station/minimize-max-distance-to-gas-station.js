/**
 * @param {number[]} stations
 * @param {number} k
 * @return {number}
 */
var minmaxGasDist = function(stations, k) {
    const canBuildK = (minDist) => {
        let count = 0;
        for (let i = 0; i < stations.length - 1; i ++) {
            const now = stations[i];
            const next = stations[i + 1];
            const dist = next - now;
            count += Math.floor(dist / minDist);
        }
        return count <= k;
    }

    let [left, right] = [0, 100_000_001];
    let answer = Infinity;

    while (left <= right) {
        const mid = (left + right) / 2;

        if (canBuildK(mid)) {
            answer = Math.min(answer, mid)
            right = mid - 0.000001;
        } else {
            left = mid + 0.000001;
        }
    }
    console.log({left, right, answer})
    return left
};