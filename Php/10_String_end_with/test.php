<?php
require 'solution.php';

$arrs = [
    [['samurai', 'ai'], true],
    [['sumo', 'omo'], false],
    [['ninja', 'ja'], true],
    [['sensei', 'i'], true],
    [['samurai', 'ra'], false],
    [['abc', 'abc'], true],
    [['abcabc', 'bc'], true],
    [['ails', 'fails'], false],
    [['fails', 'ails'], true],
    [['this', 'fails'], false],
    [['yes this will pass', ''], true],
    [['this will not pass', '`^$<>()[]*|'], false],
    [["abc\n", 'abc'], false]/**/
];

foreach ($arrs as $arr) {
    var_dump([solution($arr[0][0], $arr[0][1]), $arr[1]]);
}
