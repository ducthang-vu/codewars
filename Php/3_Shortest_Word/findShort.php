<?php
/*
Shortest Word

https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/php

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
*/


function findShort($str){
    return min(
        array_map(
            function($a) {
                return strlen($a);
            },
            explode(' ', $str)
        )
    );
}