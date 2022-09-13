/**
 * @param {number[]} data
 * @return {boolean}
 */
function getBinary(num, bit){
    return num.toString(2).padStart(bit, "0");
}


var validUtf8 = function(data) {
    function check(start, end){
        for(let i = start + 1; i <= end; i ++){
            if(i >= data.length || getBinary(data[i] >> 6) != '10'){
                return false;
            }
        }
        return true;
    }
    let start = 0;
    
    while (start < data.length){
        const now = data[start]
        if (getBinary(now >> 3) === "11110" && check(start, start + 3)){
            start += 4;
        } else if (getBinary(now >> 4) === "1110" && check(start, start + 2)){
            start += 3; 
        } else if (getBinary(now >> 5) === "110" && check(start, start + 1)){
            start += 2; 
        } else if (getBinary(now >> 7) === "0"){
            start += 1; 
        } else {
            return false;
        }
    }
    return true;
};