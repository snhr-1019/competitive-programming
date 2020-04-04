<?php
 
list($a, $b, $c) = preg_split('/ /', trim(fgets(STDIN)));
fprintf(STDOUT, '%d %d %d', $c, $a, $b);
