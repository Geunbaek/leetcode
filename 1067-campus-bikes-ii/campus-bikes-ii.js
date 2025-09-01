/**
 * @param {number[][]} workers
 * @param {number[][]} bikes
 * @return {number}
 */
var assignBikes = function(workers, bikes) {
    function calcDist(worker, bike) {
        const [wx, wy] = worker;
        const [bx, by] = bike;
        return Math.abs(bx - wx) + Math.abs(by - wy)
    }

    function calcTotalDists(){
        return workersVisit.reduce((acc, bikeIndex, workerIndex)=>{
            const bike = bikes[bikeIndex];
            const worker = workers[workerIndex];
            return acc + calcDist(worker, bike);
        }, 0)
    }

    function backtracking(depth){
        if (depth >= n) {
            answer = Math.min(answer, calcTotalDists());
            return;
        }

        for (let i = 0; i < m; i++) {
            if (bikesVisit[i]) {
                continue
            }
            workersVisit[depth] = i;
            bikesVisit[i] = true;
            backtracking(depth + 1)
            workersVisit[depth] = -1;
            bikesVisit[i] = false;
        }
    }

    const n = workers.length;
    const m = bikes.length;

    const workersVisit = new Array(n).fill(-1);
    const bikesVisit = new Array(n).fill(false);
    let answer = Infinity;
    backtracking(0);
    return answer
};