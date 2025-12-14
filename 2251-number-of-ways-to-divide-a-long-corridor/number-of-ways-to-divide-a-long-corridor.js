

/**
 * @param {string} corridor
 * @return {number}
 */
var numberOfWays = function(corridor) {
    const MOD = 1_000_000_007;

    const totalSeatCount = corridor
                            .split("")
                            .reduce((acc, cur) => cur === "S" ? acc + 1 : acc, 0);

    if (totalSeatCount < 2) return 0; 
    if (totalSeatCount % 2 !== 0) return 0;
    if (totalSeatCount === 2) return 1;

    const dp = [0];
    let nowSeatCount = 0;

    for (let i = 0; i < corridor.length; i ++) {
        const now = corridor[i];

        if (now === 'S') {
            nowSeatCount += 1;
            if (nowSeatCount > 2) {
                nowSeatCount %= 2;
                dp.push(0);
            }
        } else {
            if (nowSeatCount !== 2) continue
            dp[dp.length - 1] += 1;
        }
    }
    let answer = 1;
    for (const count of dp.slice(0, -1)) {
        answer *= (count + 1);
        answer %= MOD;
    }
    
    return answer;
};