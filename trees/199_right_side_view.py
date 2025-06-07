# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return_array = []

        # use BFS to go thought each node level by level
        queue = deque([root])
        while queue:
            level = []
            # used my logic from #102 to get nodes by level
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            # if we got some add the right most item (last in the array)
            if level:
                return_array.append(level[-1])
        
        return return_array