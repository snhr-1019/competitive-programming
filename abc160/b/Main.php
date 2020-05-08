<?php

$n = trim(fgets(STDIN));
$p1 = floor($n / 500);
print $p1 * 1000 + floor(($n - $p1 * 500) / 5) * 5;