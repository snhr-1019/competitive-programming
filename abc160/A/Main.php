<?php
 
$s = preg_split('//', trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);
print ($s[2] == $s[3] && $s[4] == $s[5]) ? "Yes" : "No";