<?php

list($a, $b) = preg_split('/ /', trim(fgets(STDIN)));
print ceil($b / $a);
