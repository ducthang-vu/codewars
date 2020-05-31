<?php
require 'positive_sum.php';

$arrs = [
    [[1, 2, 3, 4], 10],
    [[1, -2, 3, 4, 5], 13],
    [[], 0],
    [[-1, -2, -3, -4, -5], 0],
    [[-1, 2, 3, 4, -5], 9]

];

foreach ($arrs as $arr) {
    var_dump([positive_sum($arr[0]), $arr[1]]);
}
