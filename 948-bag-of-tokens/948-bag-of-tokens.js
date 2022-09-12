/**
 * @param {number[]} tokens
 * @param {number} power
 * @return {number}
 */
var bagOfTokensScore = function(tokens, power) {
    tokens.sort((a, b) => a - b);
    console.log(tokens)
    const ret = {
        answer: 0,
        score: 0,
        power,
    }
    
    while(tokens.length){
        if(ret.power >= tokens[0]){
            ret.power -= tokens.shift();
            ret.score += 1;
            ret.answer = Math.max(ret.answer, ret.score);
        } else if (ret.score >= 1){
            ret.power += tokens.pop();
            ret.score -= 1;
        } else {
            return ret.answer;
        }
        console.log(ret.power, ret.score, ret.answer)
    }
    
    return ret.answer;
};