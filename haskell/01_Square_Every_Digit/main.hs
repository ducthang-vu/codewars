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

split :: Int -> [Int]
split = map digitToInt . show . abs

square :: [Int] -> [String]
square n = [show (x ^ 2) | x <- n]

squareDigitAbs :: Int -> Int
squareDigitAbs = read . intercalate "" . square . split 

squareDigit :: Int -> Int
squareDigit a = if a >= 0 then squareDigitAbs a else (-squareDigitAbs a)


{- Solution:

module SquareDigit where
import Data.Char

squareDigit :: Int -> Int
squareDigit n
  | n < 0 = negate (squareDigit (negate n))
  | otherwise = read (show n >>= (show . (^2) . digitToInt))

-}