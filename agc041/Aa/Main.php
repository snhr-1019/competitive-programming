<?php

list($n, $a, $b) = preg_split('/ /', trim(fgets(STDIN)));

if (($b - $a) % 2 == 0) {
    print (int)(($b - $a) / 2);
} else {
    print min($n - $b, $a - 1) + 1 + ($b - $a - 1) / 2;
}