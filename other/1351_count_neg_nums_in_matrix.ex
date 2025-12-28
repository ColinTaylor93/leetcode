defmodule Solution do
  @spec count_negatives(grid :: [[integer]]) :: integer
  def count_negatives(grid) do
    row_count = length(grid)
    col_count = grid |> hd() |> length()

    start_row = 0
    start_col = col_count - 1

    traverse(grid, row_count, col_count, start_row, start_col, 0)
  end

  # Stop when we go past the last row
  defp traverse(_grid, total_rows, _total_cols, current_row, _current_col, negative_count)
       when current_row >= total_rows do
    negative_count
  end

  # Stop when we go past the first column
  defp traverse(_grid, _total_rows, _total_cols, _current_row, current_col, negative_count)
       when current_col < 0 do
    negative_count
  end

  defp traverse(
         grid,
         total_rows,
         total_cols,
         current_row,
         current_col,
         negative_count
       ) do
    current_value =
      grid
      |> Enum.at(current_row)
      |> Enum.at(current_col)

    if current_value < 0 do
      # All values below in this column are also negative
      new_count = negative_count + (total_rows - current_row)
      traverse(grid, total_rows, total_cols, current_row, current_col - 1, new_count)
    else
      # Move down to find negatives
      traverse(grid, total_rows, total_cols, current_row + 1, current_col, negative_count)
    end
  end
end
