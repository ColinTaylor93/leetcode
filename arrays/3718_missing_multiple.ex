defmodule Solution do
  @spec missing_multiple(nums :: [integer], k :: integer) :: integer
  def missing_multiple(nums, k) do
    nums_set = MapSet.new(nums)

    Stream.iterate(k, &(&1 + k))
    |> Enum.find(fn multiple -> not MapSet.member?(nums_set, multiple) end)
  end
end
