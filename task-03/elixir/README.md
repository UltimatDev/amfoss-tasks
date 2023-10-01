Forgive me for i have sinned(not exactly but still thought i'll write this)

Truth be told i ahd to copy a lot of the code here...but b4 that whatever i learned in elixir helped fix this code...i made like 5-6 approaches, learnt recursion and stuff so the task did not go to waste...
this is the only one in which most of the code i copied(but this  code didnt work) and then understood and made it better

Copied Code(For my guilty consciense)
```
defmodule Prime do
 def prime?(n) when n <= 1, do: false
 def prime?(n) when n <= 3, do: true
 def prime?(n) when rem(n, 2) == 0 or rem(n, 3) == 0, do: false
 def prime?(n), do: prime_check(n, 5)

 defp prime_check(n, i) when i * i <= n do
    cond do
      rem(n, i) == 0 or rem(n, i + 2) == 0 -> false
      true -> prime_check(n, i + 6)
    end
 end

 defp prime_check(_, _), do: true
end

defmodule Main do
 def main(args) do
    n = String.to_integer(Enum.at(args, 0))
    IO.puts("Prime numbers up to #{n}:")
    Enum.each(2..n, fn x -> if Prime.prime?(x), do: IO.puts(x) end)
 end
end
```
Thats the code i copied...IDK if it was AI generated or someone had done it but this was wrong anyways...but still i changed it and made it work really well...if you compare the checks like ```i*i<=n``` i changed it to a better logic ie. ```i<=(n/2)+1```

also the input part in main is really complicated so i changed that entire thing

```
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

```

