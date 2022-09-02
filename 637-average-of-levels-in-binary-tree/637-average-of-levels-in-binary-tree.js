/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */

const getAverage = (array) => {
    return array.reduce((acc, cur) => acc + cur, 0) / array.length;
}
var averageOfLevels = function(root) {
    const averagesMapOfLevels = new Map();
    let maxLevel = 0;
    const getValuesOfLevels = (node, level) => {
        maxLevel = Math.max(maxLevel, level);
        if(!averagesMapOfLevels[level]){
            averagesMapOfLevels[level] = [];
        }
        averagesMapOfLevels[level].push(node.val)
        if(node.left){
            getValuesOfLevels(node.left, level + 1);
        }
        if(node.right){
            getValuesOfLevels(node.right, level + 1);
        }
    }
    getValuesOfLevels(root, 0);
    console.log(averagesMapOfLevels)
    return Array.from({length: maxLevel + 1}, (_, index) => getAverage(averagesMapOfLevels[index]) )
};