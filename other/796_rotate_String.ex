defmodule Solution do
  @spec rotate_string(s :: String.t, goal :: String.t) :: boolean
  def rotate_string(s, goal) do
    String.length(s) == String.length(goal) and String.contains?(s <> s, goal)
  end
end
