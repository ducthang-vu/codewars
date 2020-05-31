<?php
/*
DNA_strand

https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/php

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

DNA_strand("ATTGC") // returns "TAACG"
DNA_strand("GTAT") // returns "CATA"
*/


function DNA_strand($dna) {
    $dic = [-2 => 'A', 2 => 'T', -1 => 'C', 1 => 'G'];
    $newStr = '';
    foreach (str_split($dna) as $char) {
        $newStr .= $dic[-array_search($char, $dic)];
    }
    return $newStr;
}


/* SOLUTION
function DNA_strand($dna) {
    return strtr($dna, 'ACGT', 'TGCA');
}
*/