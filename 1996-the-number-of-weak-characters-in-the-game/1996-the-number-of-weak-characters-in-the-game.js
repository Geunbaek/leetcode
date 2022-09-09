/**
 * @param {number[][]} properties
 * @return {number}
 */
var numberOfWeakCharacters = function(properties) {
    const n = properties.length;
    properties.sort((a, b) => {
        const [aAttack, aDefense] = a;
        const [bAttack, bDefense] = b;
        if (aAttack === bAttack){
            return aDefense - bDefense;
        }
        return bAttack - aAttack;
    })
    
    let [attack, defense] = properties[0];
    let answer = 0;
    
    for (let i = 1; i < n; i ++){
        const [curAttack, curDefense] = properties[i];
        if (attack > curAttack && defense > curDefense){
            answer += 1;
        } else {
            attack = curAttack;
            defense = curDefense;
        }
    }
    return answer;
};