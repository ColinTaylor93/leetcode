# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Union[bool, int]] is_balanced and height
        """
        def check_balance_and_height(node):
            """
            perform DFS and check balance at each node
            :type node: Optional[TreeNode]
            """
            if not node:
                # An empty tree is balanced with height 0
                return [True, 0]

            # Recursively check left and right subtrees
            left_balanced, left_height = check_balance_and_height(node.left)
            right_balanced, right_height = check_balance_and_height(node.right)

            # Current node is balanced if:
            # 1. Left subtree is balanced
            # 2. Right subtree is balanced
            # 3. The height difference between left and right is at most 1
            is_current_balanced = (
                    left_balanced and
                    right_balanced and
                    abs(left_height - right_height) <= 1
            )

            # Height of current node is max of left/right heights plus 1
            current_height = 1 + max(left_height, right_height)

            return [is_current_balanced, current_height]

        # Start DFS from root and return whether the whole tree is balanced
        return check_balance_and_height(root)[0]