defmodule Solution do
  @spec find_min(nums :: [integer]) :: integer
  def find_min(nums) do
    binary_search(nums, 0, length(nums) - 1)
  end

  # Binary search algo to find the lowest num
  defp binary_search(nums, left, right) do
    if Enum.at(nums, left) <= Enum.at(nums, right) do
      Enum.at(nums, left)
    else
      mid = div(left + right, 2)
      if Enum.at(nums, mid) > Enum.at(nums, right) do
        binary_search(nums, mid + 1, right)
      else
        binary_search(nums, left, mid)
      end
    end
  end
end
