{-
Fake Binary

https://www.codewars.com/kata/57eae65a4321032ce000002d/train/haskell

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
-}

module Codewars.Kata.FakeBinary where
import Data.Char ( digitToInt )

greater5 :: (Ord a, Num a) => a -> Bool
greater5 a = a >= 5

transform :: Char -> String
transform = show . fromEnum . greater5 . digitToInt  

fakeBin :: String -> String
fakeBin = concatMap transform

{-
SOLUTION:

fakeBin :: String -> String
fakeBin = map (\c -> if c < '5' then '0' else '1' )
-}