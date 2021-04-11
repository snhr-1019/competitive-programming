<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    list($c, $f, $x) = preg_split('/ /', trim(fgets(STDIN)));
    $result = solve($c, $f, $x);

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve($c, $f, $x) {
    $speed = 2;

    $total_time = 0;
    while(true) {
        // ファームを作らない場合
        $goal_time = $x / $speed;

        // ファームを作った場合
        $farm_time = $c / $speed;
        $speed += $f;
        $goal_time_next = $farm_time + $x / $speed;
        if ($goal_time_next > $goal_time) {
            return $total_time + $goal_time;
        }
        $total_time += $farm_time;
    }
}