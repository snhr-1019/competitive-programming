<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $result = solve(trim(fgets(STDIN)));

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve($line) {
    $char_arr = preg_split("//u", $line, -1, PREG_SPLIT_NO_EMPTY);
    $result  = 1;

    for ($i = 1; $i < count($char_arr); $i++) {
        if ($char_arr[$i - 1] != $char_arr[$i]) {
            $result++;
        }
    }
    if (end($char_arr) == '+') {
        $result--;
    }
    return $result;
}