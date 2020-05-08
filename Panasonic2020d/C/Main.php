<?php
list($a, $b, $c) = preg_split('/ /', fgets(STDIN));
$d = $c - $a - $b;
print ($d > 0 && $d * $d > 4 * $a * $b) ? "Yes" : "No";