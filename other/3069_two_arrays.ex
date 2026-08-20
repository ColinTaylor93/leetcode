defmodule Solution do
  @spec result_array(nums :: [integer()]) :: [integer()]
  def result_array([n1, n2 | rest]) do
    {arr1_rev, arr2_rev} =
      Enum.reduce(rest, {[n1], [n2]}, fn num, {[a1_head | _] = arr1, [a2_head | _] = arr2} ->
        if a1_head > a2_head do
          {[num | arr1], arr2}
        else
          {arr1, [num | arr2]}
        end
      end)

    Enum.reverse(arr1_rev) ++ Enum.reverse(arr2_rev)
  end
end
