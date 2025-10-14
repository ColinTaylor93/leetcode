defmodule Solution do
  @spec has_increasing_subarrays(nums :: [integer], k :: integer) :: boolean
  def has_increasing_subarrays(nums, k) when length(nums) < 2 * k, do: false

  def has_increasing_subarrays(nums, k) do
    n = length(nums)

    is_increasing = fn list ->
      list
      |> Enum.chunk_every(2, 1, :discard)
      |> Enum.all?(fn [a, b] -> a < b end)
    end

    0..(n - 2 * k)
    |> Enum.any?(fn a ->
      first = Enum.slice(nums, a, k)
      second = Enum.slice(nums, a + k, k)
      is_increasing.(first) and is_increasing.(second)
    end)
  end
end
