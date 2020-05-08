<?php
// WA
list($n, $x, $y) = preg_split('/ /', trim(fgets(STDIN)));
$count = array_fill(1, $n-1, 0);
for ($i=1; $i <= $n; $i++) {
    for ($j=$i+1; $j <= $n; $j++) {
        if ($i<=$x && $y<=$j) {
            $count[$j-$i-$y+$x+1]++;
        } else {
            $count[$j-$i]++;
        }
    }
}
print implode("\n", $count);