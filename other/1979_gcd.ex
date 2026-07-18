defmodule Solution do
  def find_gcd(nums), do: Enum.min_max(nums) |> then(fn {min, max} -> Integer.gcd(min, max) end)
end
