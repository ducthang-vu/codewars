<?php
require 'findShort.php';

$arrs = [
    ["bitcoin take over the world maybe who knows perhaps", 3],
    ["turns out random test cases are easier than writing out basic ones", 3]
];

foreach ($arrs as $arr) {
    var_dump([findShort($arr[0]), $arr[1]]);
}
