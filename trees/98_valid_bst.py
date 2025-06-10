# OG solution failed testcase
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        from collections import deque

        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                if node.left.val >= node.val:
                    return False
                else:
                    queue.append(node.left)
            if node.right:
                if node.right.val <= node.val:
                    return False
                else:
                    queue.append(node.right)

        return True

# new solution
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        from collections import deque

        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, left, right = queue.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                queue.append((node.left, left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))

        return True