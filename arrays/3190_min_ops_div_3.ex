defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    nums
    |> Enum.count(fn n -> rem(n, 3) != 0 end)
  end
end
