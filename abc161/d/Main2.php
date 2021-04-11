<?php

$k = trim(fgets(STDIN));


for($i = 1;; $i++) {
    if (isLunlun($i)) {
        print $i. "\n";
        $count++;
    }
    if ($count == $k) {
        print $i;
        return;
    }
}

function isLunlun($n) {
    $arr = preg_split('//', $n, -1, PREG_SPLIT_NO_EMPTY);

    for ($i=1; $i < count($arr); $i++) { 
        if (abs($arr[$i-1] - $arr[$i]) > 1) {
            return false;
        }
    }
    return true;
}