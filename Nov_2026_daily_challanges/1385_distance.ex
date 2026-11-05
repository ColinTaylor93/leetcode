defmodule Solution do
  @spec find_the_distance_value(arr1 :: [integer], arr2 :: [integer], d :: integer) :: integer
  def find_the_distance_value(arr1, arr2, d) do
    Enum.count(arr1, fn x ->
      Enum.all?(arr2, fn y -> abs(x - y) > d end)
    end)
  end
end
