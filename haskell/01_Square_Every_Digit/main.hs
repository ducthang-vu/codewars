{--

Square Every Digit

https://www.codewars.com/kata/546e2562b03326a88e000020/train/haskell

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Note: The function accepts an integer and returns an integer
--}

module SquareDigit where
import Data.Char ( digitToInt )
import Data.List ( intercalate )

fun :: Int -> [Int]
fun = map digitToInt . show . abs

inter :: [Int] -> [String]
inter n = [show (x ^ 2) | x <- n]

squareDigit :: Int -> Int
squareDigit = read . intercalate "" . inter . fun 

