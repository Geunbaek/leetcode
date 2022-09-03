/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var numsSameConsecDiff = function(n, k) {
    const answer = [];
    const dfs = (now, depth) => {
        if(depth >= n){
            answer.push(Number(now.join("")));
            return;
        }
        const lastNumber = now.at(-1);
        for(let i = 0; i < 10; i ++){
            if(Math.abs(lastNumber - i) === k){
                dfs(now.concat([i]), depth + 1);
            }
        }
    }   
    
    for(let i = 1; i < 10; i ++){
        dfs([i], 1);
    }
    return answer;
};