/**
 * @param {number[]} changed
 * @return {number[]}
 */
const getCounter = (array) => {
    const counter = new Map();
    array.forEach(num => {
        if(!counter[num]){
            counter[num] = 0;
        }
        counter[num] += 1;
    })
    return counter;
} 

var findOriginalArray = function(changed) {
    let totalCount = changed.length;
    if(totalCount % 2 !== 0) return []
    changed.sort((a, b) => a - b);
    
    const counter = getCounter(changed);
    const answer = [];
    
    for(let i = 0; i <= changed.length; i ++){
        const num = changed[i];
        if (counter[num] > 0){
            counter[num] -= 1;
            totalCount -= 1;
        } else {
            continue
        }
        
        if (counter[num * 2] && counter[num * 2] > 0){
            counter[num * 2] -= 1;
            answer.push(num);
            totalCount -= 1;
        } else {
            counter[num] += 1;
            totalCount += 1;
        }
    }
    
    return totalCount === 0 ? answer : [];
};