<?php

$n = (int) fgets(STDIN);

$arr = array_fill(1, $n, 0);
for ($i = 1; $i <= $n; $i++) { 
    $arr[(int)fgets(STDIN)]++;
}

$before = -1;
$after = -1;
for ($i = 1; $i <= $n; $i++) {
    if ($arr[$i] == 0) $before = $i;
    if ($arr[$i] == 2) $after = $i;
}
if ($before == -1) print "Correct";
else print $after . " " . $before;