<?php
// WA

$group = [];
$n = (int) fgets(STDIN);

$a = [];
for ($i = 0; $i < $n; $i++) {
    $arr = preg_split('/ /', trim(fgets(STDIN)));
    for ($j = $i+1; $j < $n; $j++) { 
        $a[$i][$j] = array_shift($arr);
    }
}

print dfs(0, $group);

function dfs($d, $group) {
    global $n, $a;
    if ($d == $n) {
        $point = 0;
        for ($i=0; $i < $n; $i++) {
            for ($j=$i+1; $j < $n; $j++) {
                if ($group[$i] == $group[$j]) {
                    $point += $a[$i][$j];
                }
            }
        }
        return $point;
    } else {
        $ans = PHP_INT_MIN;
        for ($i=0; $i < 3; $i++) { 
            $group[$d] = $i;
            $ans = max($ans, dfs($d + 1, $group));
        }
        return $ans;
    }
}
