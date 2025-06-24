# Orginal wrong answer
class Solution:

    max_total = -float('inf')

    def getPathSum(self, root:  Optional[TreeNode]) -> int:
        if not root:
            return -float('inf')
        total = root.val
        if root.left and root.left.val > 0:
            total += root.left.val
        if root.right and root.right.val > 0:
            total += root.right.val
        return total

    def getPathSumDFS(self, root: Optional[TreeNode]) -> int:
        if root:
            self.max_total = max(self.max_total, self.getPathSum(root))
            self.getPathSumDFS(root.left)
            self.getPathSumDFS(root.right)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_total = -float('inf')
        self.getPathSumDFS(root)
        return self.max_total

# used guide for help to get this answer:
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_total = float('-inf')

        def max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            current_path_sum = node.val + left_gain + right_gain
            self.max_total = max(self.max_total, current_path_sum)
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_total



