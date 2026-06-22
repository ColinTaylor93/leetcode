defmodule Solution do
  @spec max_number_of_balloons(text :: String.t) :: integer
  def max_number_of_balloons(text) do
    if String.length(text) < 7 do
      0
    else
        frequencies =
            text
            |> String.graphemes()
            |> Enum.reduce(%{}, fn char, acc ->
                Map.update(acc, char, 1, &(&1 + 1))
            end)

        b_count = Map.get(frequencies, "b", 0)
        a_count = Map.get(frequencies, "a", 0)
        l_count = div(Map.get(frequencies, "l", 0), 2) # Divide 'l' by 2
        o_count = div(Map.get(frequencies, "o", 0), 2) # Divide 'o' by 2
        n_count = Map.get(frequencies, "n", 0)

        Enum.min([b_count, a_count, l_count, o_count, n_count])
    end
  end
end
