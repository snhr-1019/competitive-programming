<?php

$n = trim(fgets(STDIN));
$arr = preg_split('/ /', trim(fgets(STDIN)));
$count = [];
$combi = [];
for ($i=1; $i <= $n; $i++) { 
    $count[$arr[$i-1]]++;
}
$sum = 0;
for ($i=1; $i <= $n; $i++) { 
    $sum += $combi[$i] = $count[$i] * ($count[$i]-1) / 2;
}
for ($i=1; $i <= $n; $i++) {
    print $sum - $combi[$arr[$i-1]] + ($count[$arr[$i-1]]-1) * ($count[$arr[$i-1]]-2) / 2 . "\n";
}
