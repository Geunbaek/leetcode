/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    function toBe(arg) {
        if (val !== arg) {
            throw Error("Not Equal");
        }
        return true;
    }
    function notToBe(arg) {
        if (val === arg) {
            throw Error("Equal");
        }
        return true;
    }

    return {
        toBe, 
        notToBe
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */