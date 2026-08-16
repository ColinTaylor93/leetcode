# This was the solution I orginally used but it failed this test case:
# piles = [3,2,10,4]

# I learned after that alice always wins if she plays optimally, so I just return true in my submitted solution.

defmodule Solution do
  def stone_game(piles) do
    play(piles, 0, 0, _turn = 1)
  end

  defp play([], alice_score, bob_score, _turn) do
    alice_score > bob_score
  end

  defp play(piles, alice_score, bob_score, turn) do
    {stone, is_first} = best_pile(piles)
    remaining_piles = remove_pile(piles, is_first)

    if rem(turn, 2) == 1 do
      # Alice's turn
      play(remaining_piles, alice_score + stone, bob_score, turn + 1)
    else
      # Bob's turn
      play(remaining_piles, alice_score, bob_score + stone, turn + 1)
    end
  end

  defp best_pile([single]) do
    {single, true}
  end

  defp best_pile([first, last]) do
    if first > last do
      {first, true}
    else
      {last, false}
    end
  end

  defp best_pile(piles) do
    first = hd(piles)
    last = List.last(piles)

    cond do
      first > last ->
        {first, true}

      first < last ->
        {last, false}

      true ->
        second = Enum.at(piles, 1)
        second_to_last = Enum.at(piles, -2)

        if second > second_to_last do
          {last, false}
        else
          {first, true}
        end
    end
  end

  defp remove_pile([_head | tail], _is_first = true), do: tail
  defp remove_pile(piles, _is_first = false), do: Enum.drop(piles, -1)
end
