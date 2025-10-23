/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function(s) {
    const oper = (s) => {
        let num = ""
        for (let i = 0; i < s.length - 1; i++) {
            num += ((parseInt(s[i]) + parseInt(s[i + 1])) % 10).toString()
        }

        return num;
    }

    let answer = s;
    while (answer.length > 2) {
        answer = oper(answer)
    }

    return answer[0] === answer[1]
};