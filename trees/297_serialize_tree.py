class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        return_list = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                return_list.append("null")
            else:
                return_list.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(return_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_values = data.split(",")
        if tree_values[0] == "null":
            return None

        root = TreeNode(int(tree_values[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if tree_values[index] != "null":
                node.left = TreeNode(int(tree_values[index]))
                queue.append(node.left)
            index += 1
            if tree_values[index] != "null":
                node.right = TreeNode(int(tree_values[index]))
                queue.append(node.right)
            index += 1

        return root