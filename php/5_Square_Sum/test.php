<?php
require 'square_sum.php';

$arrs = [
    [[1, 2], 5],
    [[0, 3, 4, 5], 50],
    [[], 0],
    [[-1, -2], 5],
    [[-1, 0, 1], 2]
];

foreach ($arrs as $arr) {
    var_dump([square_sum($arr[0]), $arr[1]]);
}
