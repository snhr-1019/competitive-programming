<?php
list($h, $w, $k) = preg_split('/ /', trim(fgets(STDIN)));
$cake;
for ($i=0; $i < $h; $i++) { 
    $cake[] = preg_split('//', trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);
}
