const calcArea = (w, h) => w * h;

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    const n = height.length;


    let [left, right] = [0, n - 1];
    let size = calcArea(right - left, Math.min(height[left], height[right]));

    while (left < right) {
        if (height[left] < height[right]) {
            left += 1;
        } else {
            right -= 1;
        }
        size = Math.max(size, calcArea(right - left, Math.min(height[left], height[right])))
    }
    return size
}; 