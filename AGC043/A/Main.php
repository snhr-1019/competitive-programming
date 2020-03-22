<?php

list($h, $w) = preg_split('/ /', trim(fgets(STDIN)));

$map = [];
$dp = [];
for ($i = 0; $i < $h; $i++) { 
    $map[$i] =  preg_split('//', trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);
}

print (ceil(move(0, 0, $map[0][0] == "#" ? 1 : 0) / 2));

function move($r, $c, $count) {
    global $h, $w, $map, $dp;
    if ($r == $h -1 && $c == $w - 1) return $count;
    $p1 = $p2 = PHP_INT_MAX;
    if ($c < $w - 1) $p1 = move($r, $c+1, $map[$r][$c] == $map[$r][$c+1] ? $count : $count+1);
    if ($r < $h - 1) $p2 = move($r+1, $c, $map[$r][$c] == $map[$r+1][$c] ? $count : $count+1);
    return min($p1, $p2);
}