<?php
 
list($n, $m) = preg_split('/ /', trim(fgets(STDIN)));
$a = preg_split('/ /', trim(fgets(STDIN)));
rsort($a, SORT_NUMERIC);
$sum = 0;
for ($i=0; $i < $n; $i++) {
    $sum += $a[$i];
}
for ($i=0; $i < $m; $i++) { 
    if ($a[$i] < $sum / (4*$m)) {
        print "No";
        return;
    }
}
print "Yes";
return;
