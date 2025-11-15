
var TwoSum = function() {
    this.nums = [];
    this.isSorted = false;
};

/** 
 * @param {number} number
 * @return {void}
 */
TwoSum.prototype.add = function(number) {
    this.nums.push(number);
    this.isSorted = false;
};

/** 
 * @param {number} value
 * @return {boolean}
 */
TwoSum.prototype.find = function(value) {
    if (!this.isSorted) {
        this.nums.sort((a, b) => a - b);
        this.isSorted = true;
    }

    
    let [l, r] = [0, this.nums.length - 1];
    
    while (l < r) {
        const sum = this.nums[l] + this.nums[r];
        if (sum > value) {
            r -= 1;
        } else if (sum < value) {
            l += 1;
        } else {
            return true;
        }
    }
    return false;
};

/** 
 * Your TwoSum object will be instantiated and called as such:
 * var obj = new TwoSum()
 * obj.add(number)
 * var param_2 = obj.find(value)
 */