<?php
/*
Square(n) Sum

https://www.codewars.com/kata/515e271a311df0350d00000f/train/php

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
*/

function square_sum($numbers) : int {
    return array_reduce($numbers, function($a, $b) {return $a + $b**2;}, 0);
}


/* Alternative solution 
function square_sum($n) : int {
    return array_sum(array_map(function($v){return $v * $v;}, $n));
}
*/