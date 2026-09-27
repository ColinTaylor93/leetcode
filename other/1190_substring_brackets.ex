defmodule Solution do
  @spec reverse_parentheses(s :: String.t) :: String.t
  def reverse_parentheses(s) do
    s
    |> String.graphemes()
    |> Enum.reduce([], fn
      ")", stack ->
        {inside_parentheses, ["(" | remaining_stack]} = Enum.split_while(stack, fn char -> char != "(" end)
        Enum.reverse(inside_parentheses) ++ remaining_stack

      char, stack ->
        [char | stack]
    end)
    |> Enum.reverse()
    |> Enum.join("")
  end
end
