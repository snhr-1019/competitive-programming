<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $result = solve(trim(fgets(STDIN)));

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve($n) {
    if ($n == 0) return "INSOMNIA";
    $arr = [];
    for ($i = 1;; $i++) {
        foreach (preg_split("//u", ($n * $i), -1, PREG_SPLIT_NO_EMPTY) as $num) {
            if (!array_key_exists($num, $arr)) {
                $arr[$num] = true;
            }
        }
        if (count($arr) == 10) break;
    }
    return $n * $i;
}
