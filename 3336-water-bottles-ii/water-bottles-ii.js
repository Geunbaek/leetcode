/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var maxBottlesDrunk = function(numBottles, numExchange) {
    let empty = 0;
    let answer = 0;
    
    while (true) {
        empty += numBottles;
        answer += numBottles;
        numBottles = 0;

        let buy = 0;

        while (empty >= numExchange) {
            empty -= numExchange;
            numBottles += 1;
            numExchange += 1;
            buy += 1;
        }
        if (buy === 0) break;
    }

    return answer;
};