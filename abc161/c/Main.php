<?php
 
list($x, $k) = preg_split('/ /', trim(fgets(STDIN)));
print min(
    $x % $k ,
    $k - ($x % $k)
);
