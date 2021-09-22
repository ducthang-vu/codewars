{-
Returning Strings

Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

SQL: return results in a column named greeting

[Make sure you type the exact thing I wrote or the program may not execute properly]
-}


module Codewars.Kata.Negative where

makeNegative :: (Num a, Ord a) => a -> a
makeNegative n = if n > 0 then negate n else n

{- 
Solution
makeNegative = negate . abs
-}
