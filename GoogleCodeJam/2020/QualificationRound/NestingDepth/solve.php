<?php
$problem_count = trim(fgets(STDIN));

for ($a = 0; $a < $problem_count; $a++) {
    echo 'Case #' . ($a + 1) . ': ';
    solve();
    echo "\n";
}

function solve() {
    $arr =  preg_split('//', trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);
    outputOpen($arr[0]);
    echo $arr[0];
    for ($i=1; $i < count($arr); $i++) { 
        if ($arr[$i-1] < $arr[$i]) {
            outputOpen($arr[$i]-$arr[$i-1]);
        } else if ($arr[$i-1] > $arr[$i]) {
            outputClose($arr[$i-1]-$arr[$i]);
        }
        echo $arr[$i];
    }
    outputClose($arr[count($arr)-1]);
}

function outputOpen($n) {
    for ($i=0; $i < $n; $i++) { 
        echo '(';
    }
}
function outputClose($n) {
    for ($i=0; $i < $n; $i++) { 
        echo ')';
    }
}
