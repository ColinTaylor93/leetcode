# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # use BFS to get an array of levels and values from them
        # from my soultion to #102
        tree_as_array = []
        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                tree_as_array.append(level)
        
        # get the total for each row in the tree, keep in array
        row_totals = [sum(sublist) for sublist in tree_as_array]
        # sort the array and return the largets k value
        return sorted(row_totals, reverse=True)[k - 1]