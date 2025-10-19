defmodule Solution do
  def convert(s, num_rows) do
    # Handle simple edge cases directly
    if num_rows <= 1 or num_rows >= String.length(s) do
      s
    else
      # Split the input string into a list of characters (graphemes)
      chars = String.graphemes(s)

      # Initialize:
      # - rows: a list of empty strings, one per row
      # - row: current row index (starts at 0)
      # - dir: direction (1 = down, -1 = up)
      initial_state = {List.duplicate("", num_rows), 0, 1}

      {rows, _row, _dir} =
        Enum.reduce(chars, initial_state, fn ch, {rows, row, dir} ->
          # Add current character to its row
          updated_rows = List.update_at(rows, row, &(&1 <> ch))

          # Move up or down
          cond do
            row == 0 ->
              {updated_rows, row + 1, 1}

            row == num_rows - 1 ->
              {updated_rows, row - 1, -1}

            true ->
              {updated_rows, row + dir, dir}
          end
        end)

      # Combine all rows into one final string
      Enum.join(rows)
    end
  end
end
