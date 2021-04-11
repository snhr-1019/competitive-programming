<?php

$k = trim(fgets(STDIN));

$que = [];
$count = 0;
for($i = 1; $i <= 9; $i++) {
    $que[] = $i;
    $count++;
    if ($count == $k) {
        print $i;
        return;
    }
}

while (true) {
    $num = array_shift($que);
    $last = $num % 10;
    if ($last != 0) bfs(10*$num+$last-1);
    bfs(10*$num+$last);
    if ($last != 9) bfs(10*$num+$last+1);
}

function bfs($num) {
    global $que, $count, $k;
    $que[] = $num;
    $count++;
    if ($count == $k) {
        print $num;
        exit;
    }
}
