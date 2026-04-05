defmodule Solution do
  @spec judge_circle(moves :: String.t) :: boolean
  def judge_circle(moves) do
    {final_x, final_y} = 
      moves
      |> String.graphemes()
      |> Enum.reduce({0, 0}, fn char, {x, y} ->
        case char do
          "U" -> {x, y + 1}
          "D" -> {x, y - 1}
          "L" -> {x - 1, y}
          "R" -> {x + 1, y}
        end
      end)

    final_x == 0 && final_y == 0
  end
end