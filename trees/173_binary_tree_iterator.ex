# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule BSTIterator do
  @spec init_(root :: TreeNode.t | nil) :: any
  def init_(root) do
    stack = push_left(root, [])
    Process.put(:bst_stack, stack)
    nil
  end

  @spec next() :: integer
  def next() do
    [node | rest] = Process.get(:bst_stack)

    # If the node has a right subtree, push its left chain
    new_stack =
      case node.right do
        nil -> rest
        right -> push_left(right, rest)
      end

    Process.put(:bst_stack, new_stack)
    node.val
  end

  @spec has_next() :: boolean
  def has_next() do
    Process.get(:bst_stack) != []
  end

  # Helper: push node and all its left children onto the stack
  defp push_left(nil, stack), do: stack

  defp push_left(node, stack) do
    push_left(node.left, [node | stack])
  end
end

# Your functions will be called as such:
# BSTIterator.init_(root)
# param_1 = BSTIterator.next()
# param_2 = BSTIterator.has_next()

# BSTIterator.init_ will be called before every test case, in which you can do some necessary initializations.
