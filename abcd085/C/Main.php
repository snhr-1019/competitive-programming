<?php

list($n, $sum) = preg_split('/ /', trim(fgets(STDIN)));
for ($x = 0; $x <= $n ; $x++) {
    for ($y = 0; $y <= $n - $x; $y++) {
        $z = $n - $x - $y;
        if ($sum == $x * 10000 + $y * 5000 + $z * 1000) {
            printf('%d %d %d', $x, $y, $z);
            return;
        }
    } 
}

printf('%d %d %d', -1, -1, -1);
