/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const n1 = arr1.length;
    const n2 = arr2.length;

    arr1.sort((a, b) => a.id - b.id);
    arr2.sort((a, b) => a.id - b.id);

    let [left, right] = [0, 0];
    const ret = [];

    while (left < n1 && right < n2) {
        if (arr1[left].id < arr2[right].id) {
            ret.push(arr1[left]);
            left += 1;
        } else if (arr1[left].id > arr2[right].id) {
            ret.push(arr2[right]);
            right += 1;
        } else {
            ret.push({...arr1[left], ...arr2[right]});
            left += 1;
            right += 1;
        }
    }

    while (left < n1) {
        ret.push(arr1[left]);
        left += 1;
    }

    while (right < n2) {
        ret.push(arr2[right]);
        right += 1;
    }
    return ret
};