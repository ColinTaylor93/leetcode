class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # edge case for nothing
        if not root:
            return 0

        self.res = 0

        def dfs(node):
            """
            Get the depth of a binary tree when given a node
            :type node: Optional[TreeNode]
            :rtype: int
            """
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        # depth-first-search through the tree and return the depth
        dfs(root)
        return self.res


## Original failing solution: time limit exceeded

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # edge case for nothing
        if not root:
            return 0

        # Get the distance between the root for the left side and the right side and add them
        left_side = self.getHeightBinaryTree(root.left)
        right_side = self.getHeightBinaryTree(root.right)
        diameter = left_side + right_side

        # it is possible of the longest distance to be entirly on one side so check that too
        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))

        # return the bigger one
        return max(diameter, sub)


    def getHeightBinaryTree(self, root):
        """
        Get the depth of a binary tree when given a node
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        else:
            return 1 + max(self.getHeightBinaryTree(root.left), self.getHeightBinaryTree(root.right))