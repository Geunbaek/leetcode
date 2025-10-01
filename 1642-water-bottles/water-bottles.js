/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    let empty = 0;
    let answer = 0;
    
    while (true) {
        empty += numBottles;
        answer += numBottles;
        numBottles = 0;

        const buy = Math.floor(empty / numExchange);
        numBottles += buy;
        empty -= buy * numExchange;
        if (buy === 0) break;
    }
    return answer;
};