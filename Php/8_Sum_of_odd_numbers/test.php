<?php
require 'rowSumOddNumbers.php';

$arrs = [
    [1, 1],
    [2, 8],
    [13, 2197],
    [19, 6859],
    [41, 68921],
    [42, 74088],
    [74, 405224],
    [86, 636056],
    [93, 804357],
    [101, 1030301]
];

foreach ($arrs as $arr) {
    var_dump([rowSumOddNumbers($arr[0]), $arr[1]]);
}
