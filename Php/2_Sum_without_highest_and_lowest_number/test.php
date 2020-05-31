<?php
require 'sumArray.php';

$arrs = [
    [[6, 2, 1, 8, 10], 16],
    [[1, 1, 11, 2, 3], 6]
];

foreach ($arrs as $arr) {
    var_dump([sumArray($arr[0]), $arr[1]]);
}
