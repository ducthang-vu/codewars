<?php
require 'invert.php';

$arrs = [
    [[1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]],
    [[1, -2, 3, -4, 5], [-1, 2, -3, 4, -5]],
    [[], []],
    [[0], [0]]
];


foreach ($arrs as $arr) {
    var_dump([invert($arr[0]), $arr[1]]);
}
