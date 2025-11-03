/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function(colors, neededTime) {
    const stack = [];
    let answer = 0;

    for (let i = 0; i < colors.length; i++){
        const color = colors[i];
        const time = neededTime[i];

        while (
            stack.length 
            && stack.at(-1).color === color 
            && stack.at(-1).time < time
        ) {
            answer += stack.pop().time;
        }
        if (stack.at(-1)?.color !== color) {
            stack.push({color, time, i});
        } else {
            answer += time;
        }
    }
    return answer;
};