defmodule Solution do
  @spec my_pow(x :: float, n :: integer) :: float
  def my_pow(x, n) do
    # Handle negative exponents by inverting x and making n positive
    {x, n} = if n < 0, do: {1.0 / x, -n}, else: {x, n}

    # Initialize result as 1 (since anything ^0 = 1)
    result = 1.0

    # Loop until n becomes 0
    my_pow_iter(x, n, result)
  end

  # Helper function for iteration
  defp my_pow_iter(_x, 0, result), do: result
  defp my_pow_iter(x, n, result) do
    # If n is odd, multiply result by current x
    result =
      if rem(n, 2) == 1 do
        result * x
      else
        result
      end

    # Square x (since we're halving the exponent)
    x = x * x

    # Divide n by 2 (integer division)
    n = div(n, 2)

    # Continue looping
    my_pow_iter(x, n, result)
  end
end
