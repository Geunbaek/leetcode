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
 * @return {TreeNode}
 */
var pruneTree = function(root) {
    const dfs = (node, index) => {
        let hasLeftChild = false;
        let hasRightChild = false;
        if(node.left){
            hasLeftChild ||= dfs(node.left, index * 2 + 1)
            if (!hasLeftChild) {
                node.left = null;
            }
        }
        if(node.right){
            hasRightChild ||= dfs(node.right, index * 2 + 2 )
            if (!hasRightChild) {
                node.right = null;
            }
        }
        return node.val || hasLeftChild || hasRightChild
    }
    
    if(!dfs(root, 0)){
        root = null;
    }
    return root
};