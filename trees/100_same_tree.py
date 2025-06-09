# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque

        # make queue for both tree, going to use BFS to search them
        queue_tree_p = deque([p])
        queue_tree_q = deque([q])

        while queue_tree_p and queue_tree_q:
            # pop a node of both trees
            node1 = queue_tree_p.popleft()
            node2 = queue_tree_q.popleft()

            # if they're both none, move on
            if node1 is None and node2 is None:
                continue

            # if only 1 is none, its a diffrence and the answer is false
            if  node1 is None or node2 is None:
                return False

            # if the values are diffrent, return false
            if node1.val != node2.val:
                return False

            # add the new nodes to the respective queues
            queue_tree_p.append(node1.left)
            queue_tree_p.append(node1.right)
            queue_tree_q.append(node2.left)
            queue_tree_q.append(node2.right)

        # if we got here they must be the same
        return True