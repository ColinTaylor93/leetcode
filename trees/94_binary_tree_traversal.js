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
var inorderTraversal = function(root) {
    let output = [];

    function getValue(node) {
        if (!node) {
            return;
        }
        getValue(node.left)
        output.push(node.val)
        getValue(node.right)
    }

    getValue(root)
    return output
};