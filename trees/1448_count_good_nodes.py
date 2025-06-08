# NOTE: this was a bad answer, got beats 9.86% on speed despite O(n) complexity

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        good_nodes_counter = 0

        queue = deque()
        queue.append((root,-float('inf')))

        while queue:
            node, max_value = queue.popleft()
            if node:
                if node.val >= max_value:
                    good_nodes_counter += 1
                new_max = max(max_value, node.val)
                queue.append((node.left, new_max))
                queue.append((node.right, new_max))

        return good_nodes_counter
