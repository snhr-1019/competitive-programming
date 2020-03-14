<?php
$n = (int)fgets(STDIN);
dfs("", 0, $n);

function dfs($str, $mx) {
    global $n;
    if (strlen($str) == $n) {
        print $str . "\n";
        return;
    }

    for ($i = 0; $i <= $mx; $i++) {
        dfs($str . chr(97 + $i), ($i == $mx) ? $mx + 1 : $mx);
    }
}