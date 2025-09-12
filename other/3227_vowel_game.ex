defmodule Solution do
  @spec does_alice_win(s :: String.t) :: boolean
  def does_alice_win(s) do
    vowels = MapSet.new(["a", "e", "i", "o", "u"])

    vowel_count =
      s
      |> String.downcase()
      |> String.graphemes()
      |> Enum.filter(&MapSet.member?(vowels, &1))
      |> length()

    vowel_count > 0
  end
end