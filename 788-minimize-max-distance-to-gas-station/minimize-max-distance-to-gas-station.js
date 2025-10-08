/**
 * @param {number[]} stations
 * @param {number} k
 * @return {number}
 */
var minmaxGasDist = function(stations, k) {
    const canBuildK = (minDist) => stations
        .reduce((count, station, i) => {
            if (i === stations.length - 1) return count;
            return count + Math.floor((stations[i + 1] - station) / minDist);
        }, 0) <= k

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