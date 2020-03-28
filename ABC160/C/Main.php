<?php
 
list($k, $n) = preg_split('/ /', trim(fgets(STDIN)));
$a = preg_split('/ /', trim(fgets(STDIN)));

$max = $a[0] - $a[$n-1] + $k;
for ($i=1; $i < $n-1; $i++) { 
    $max = max($max, $a[$i+1] - $a[$i]);
}
print $k - $max;