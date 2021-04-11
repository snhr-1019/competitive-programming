<?php

list($n, $m) = preg_split('/ /', trim(fgets(STDIN)));
print $n * ($n-1) / 2 + $m * ($m-1) / 2;
