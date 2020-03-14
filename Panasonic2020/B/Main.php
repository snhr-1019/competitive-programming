<?php
list($h, $w) = preg_split('/ /', fgets(STDIN));
// corner caseの考慮が漏れていた
print ($h == 1 || $w == 1) ? 1 : (int)ceil($h * $w / 2);
