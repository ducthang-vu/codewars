<?php
/* 
Sum of positive

https://www.codewars.com/kata/5715eaedb436cf5606000381/train/php

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
*/


function positive_sum($arr) {
    return array_reduce(
            $arr, 
            function($a, $b) {
                $b < 0 && $b = 0;
                return $a + $b;
            }
        );
}


/* SOLUTION 
function positive_sum($a) {
    return array_sum(array_filter($a, function ($n) {return $n > 0;}));
}
*/
