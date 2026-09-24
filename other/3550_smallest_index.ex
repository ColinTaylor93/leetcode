defmodule Solution do
  @spec smallest_index(nums :: [integer]) :: integer
  def smallest_index(nums) do
    nums
    |> Enum.with_index()
    |> Enum.find_value(-1, fn {num, i} ->
      if sum_digits(num) == i, do: i, else: nil
    end)
  end

  defp sum_digits(num) do
    num
    |> Integer.digits()
    |> Enum.sum()
  end
end
