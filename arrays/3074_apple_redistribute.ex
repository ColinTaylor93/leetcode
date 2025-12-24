defmodule Solution do
@spec minimum_boxes(apple :: [integer], capacity :: [integer]) :: integer
def minimum_boxes(apple, capacity) do
    total_apples = Enum.sum(apple)

    result =
      capacity
        |> Enum.sort(:desc)
        |> Enum.with_index()
        |> Enum.reduce_while(0, fn {cap, index}, total_cap ->
            new_total = total_cap + cap

            if new_total >= total_apples do
                {:halt, {:found, index + 1}}
            else
                {:cont, new_total}
            end
        end)

    case result do
      {:found, count} -> count
      _ -> length(capacity)
    end
  end
end
