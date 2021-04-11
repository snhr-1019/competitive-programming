<?php

list($h, $w) = preg_split('/ /', trim(fgets(STDIN)));

$map = [];
$dp = [];
for ($i = 0; $i < $h; $i++) { 
    $map[$i] =  preg_split('//', trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);
}

print (ceil(score($h - 1, $w - 1) / 2));

function score($r, $c) {
    global $h, $w, $map, $dp;
    if (isset($dp[$r][$c])) return $dp[$r][$c];

    if ($r == 0 && $c == 0) return ($map[$r][$c] == "#") ? 1 : 0;

    $s1 = $s2 = PHP_INT_MAX;
    if ($r != 0) {
        $s1 = score($r-1, $c);
        if ($map[$r-1][$c] != $map[$r][$c]) $s1++;
    }
    
    if ($c != 0) {
        $s2 = score($r, $c-1);
        if ($map[$r][$c-1] != $map[$r][$c]) $s2++;
    }

    return $dp[$r][$c] = min($s1, $s2);
}