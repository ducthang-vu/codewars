<?php
require 'tower_builder.php';

$arrs = [
    [1, '*'],
    [3, [
        '  *  ',
        ' *** ',
        '*****'
    ]],
    [6, [
        '     *     ', 
        '    ***    ', 
        '   *****   ', 
        '  *******  ', 
        ' ********* ', 
        '***********'
    ]]
];

foreach ($arrs as $arr) {
    var_dump([tower_builder($arr[0]), $arr[1]]);
}
