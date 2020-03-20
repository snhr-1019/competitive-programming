<?php

$n = (int)(fgets(STDIN));
$dp = [];
$a = [];
$b = [];
$c = [];
for ($i=0; $i < $n; $i++) { 
    list($a[], $b[], $c[]) = preg_split('/ /', trim(fgets(STDIN)));
}

print dfs(0, -1);

function dfs($d, $preChoice) {
    global $dp, $n, $a, $b, $c;

    if ($d == $n) return 0;

    if ($preChoice != 0) $chooseA = dfs($d+1, 0) + $a[$d];
    if ($preChoice != 1) $chooseB = dfs($d+1, 0) + $b[$d];
    if ($preChoice != 2) $chooseC = dfs($d+1, 0) + $c[$d];

    return max([$chooseA, $chooseB, $chooseC]);
}