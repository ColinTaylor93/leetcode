# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        return_array = []

        # breadth-first-search to go through the tree
        queue = deque([root])
        while queue:
            # whatever is in the queue so far is for that level so far
            level = []
            # so loop through that and add to `level`
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    # Add node to level
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            # Add `level` to return array
            if level:
                return_array.append(level)

        return return_array
