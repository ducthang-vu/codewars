<?php
require 'DNA_strand.php';

$arrs = [
    ['AAAA', 'TTTT'],
    ['TTTT', 'AAAA'],
    ['ATTGC', 'TAACG'],
    ['TAACG', 'ATTGC'],
    ['GTAT', 'CATA'],
    ['CATA', 'GTAT']
];

foreach ($arrs as $arr) {
    var_dump([DNA_strand($arr[0]), $arr[1]]);
}
