<?php
/*
Buil Tower

https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/php

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Lua: returns a Table;
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
*/


function tower_builder(int $n): array {
    $output = [];
    for ($i = 1; $i <= $n; $i++) {
        $output[] = str_repeat(' ', $n - $i) . str_repeat('*', 2*($i - 1) + 1) . str_repeat(' ', $n - $i);
    }
    return $output;
}