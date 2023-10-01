defmodule Prime do
 def prime?(n) when n <= 1, do: false
 def prime?(n) when n <= 3, do: true
 def prime?(n) when rem(n, 2) == 0 or rem(n, 3) == 0, do: false
 def prime?(n), do: prime_check(n, 5)

 defp prime_check(n, i) when i <= (n/2)+1 do
    cond do
      rem(n, i) == 0 or rem(n, i + 2) == 0 -> false
      true -> prime_check(n, i + 6)
    end
 end

 defp prime_check(_, _), do: true
end

x=IO.gets("Enter N")
y=String.trim(x)
n = String.to_integer(y)
IO.puts("Prime numbers up to #{n}:")
Enum.each(2..n, fn x -> if Prime.prime?(x), do: IO.puts(x) end)
