/**
 * @param {number[][]} workers
 * @param {number[][]} bikes
 * @return {number}
 */
var assignBikes = function(workers, bikes) {
    const X = 0, Y = 1;
    const get = (mask, i) => (1 << i) & mask;
    const set = (mask, i) => (1 << i)|mask;
    const unset = (mask, i) => (1 << i)^mask; // unsets if set. if is not set will set it

    const getDistance = (pos1, pos2) => {
        return Math.abs(pos1[X]-pos2[X]) + Math.abs(pos1[Y]-pos2[Y]);
    };

    const memo = {};
    const dp = (workerI, bikeMask) => {
        if (workerI < 0) return 0;
        const key = `${workerI}.${bikeMask}`;
        if (key in memo) return memo[key];

        let min = Infinity;
        for (let i=0;i<bikes.length;i++) {
            if (get(bikeMask, i) === 0) {
                const currDistance = getDistance(
                    workers[workerI],
                    bikes[i]
                );
                min = Math.min(
                    min, 
                    currDistance + dp(workerI-1, set(bikeMask, i))
                );
            }
        }

        memo[key] = min;
        return memo[key];
    };
    
    const result = dp(workers.length-1, 0);

    return result;
};

























