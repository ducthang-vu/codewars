{-
Mumbling

https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/haskell

This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

-}

module Codewars.G964.Accumule where
import Data.List ( intercalate )
import Data.Char ( toLower, toUpper )

enum :: [Char] -> [(Int, Char)]
enum = zip [1..] 

capitalized :: [Char] -> [Char]
capitalized (head:tail) = toUpper head : map toLower tail

accum :: [Char] -> [Char]
accum s = intercalate "-" [ capitalized (concat $ replicate index [letter]) | (index, letter) <- enum s ]
