<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $result = solve(trim(fgets(STDIN)));

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve($n) {
    $arr = preg_split("/ /", $n, -1, PREG_SPLIT_NO_EMPTY);
    foreach ($arr as $value) {
      # code...
    }
     $max = findMax($arr);
     return $max;
}

function findMax(array $arr)
{
    $max = max($arr);
    $arrFind = array_keys($arr, $max);
    $key = array_rand($arrFind, 1);
    $arr[$key]--;
    return $arrFind[$key];
}
